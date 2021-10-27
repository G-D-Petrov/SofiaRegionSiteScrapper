from pathlib import Path
import json
import requests
from parsers import parsers_dict
from rich import print

def load_sites_dict():
    """ Tries to load the sites.json from the config folder into a python dict """
    sites_json_path = Path("config/sites.json")
    with open(sites_json_path, "r") as fp:
        sites_dict = json.load(fp)

    return sites_dict

def main():
    sites_dict = load_sites_dict()
    TALKS_URL = 'talks_url'
    
    for region in sites_dict:
        # If the region name has changed or if we haven't written a parser yet
        # we cannot handle this region
        if region not in parsers_dict or not parsers_dict[region] or TALKS_URL not in sites_dict[region]:
            continue 
        
        parser = parsers_dict[region]

        response = requests.get(sites_dict[region][TALKS_URL])
        response.encoding = 'utf-8' 
        html_str = response.text
        feed_list = parser(html_str)
        print(feed_list)

if __name__ == "__main__":
    main()