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
    parser = parsers_dict['Sredec']
    response = requests.get(sites_dict['Sredec']['talks_url'])
    response.encoding = 'utf-8' 
    html_str = response.text
    feed_list = parser(html_str)
    print(feed_list)

if __name__ == "__main__":
    main()