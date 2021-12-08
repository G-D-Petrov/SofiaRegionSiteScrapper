import os
from pathlib import Path
import json
from tqdm import tqdm
import requests
import time
from parsers import parsers_dict
from rich import print
from mails import send_mail

def load_sites_dict():
    """ Tries to load the sites.json from the config folder into a python dict """
    sites_json_path = Path("config/sites.json")
    with open(sites_json_path, "r") as fp:
        sites_dict = json.load(fp)

    return sites_dict

def parse_sites(sites_dict, cache_path):
    TALKS_URL = 'talks_url'
    diff_dict = dict()
    
    for region in tqdm(sites_dict):
        # If the region name has changed or if we haven't written a parser yet
        # we cannot handle this region
        if region not in parsers_dict or not parsers_dict[region] or TALKS_URL not in sites_dict[region]:
            continue 
        
        parser = parsers_dict[region]

        response = requests.get(sites_dict[region][TALKS_URL])
        response.encoding = 'utf-8' 
        html_str = response.text
        feed_list = parser(html_str)
        
        with open(cache_path / region, "r", encoding='utf-8') as fp:
            past_list = json.load(fp)
        
        diff_list = [item for item in feed_list if item not in past_list]
        
        if len(diff_list) == 0:
            continue
        
        diff_dict[region] = diff_list
        
        with open(cache_path / region, "w+", encoding='utf-8') as fp:
            json.dump(feed_list, fp, indent=4, default=str, ensure_ascii=False)
            
    return diff_dict

def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--address_from',
                        help='Mail address to act as a sender of the final mail',
                        default="petrov.d.george.bot@gmail.com")
    
    parser.add_argument('--address_to',
                        help='Mail address to send the final mail to',
                        default="petrov.d.george@gmail.com")
    
    parser.add_argument('--send_mail',
                        help='Should we send mails? (default: True)',
                        default=True)
    
    return parser.parse_args()

def main():
    args = parse_args()
    sites_dict = load_sites_dict()
    cache_path = Path('cache/')
    if not cache_path.exists():
        os.mkdir(cache_path)
        
    diff_dict = parse_sites(sites_dict, cache_path)
    
    if diff_dict:
        print(f"New messages to publish: {diff_dict}")
        send_mail(diff_dict, args.address_from, args.address_to)
    else:
        print("Nothing new to publish")

if __name__ == "__main__":
    main()