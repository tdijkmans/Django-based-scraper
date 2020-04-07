import sys
import os
import django
import requests
from bs4 import BeautifulSoup
import re
import json

sys.path.append('/recipefree/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'recipefree.settings'
django.setup()

import pandas as pd
from collector.models import SmulWebRecipe, SmulWebPage


def get_smulwebpage(page_nr):
    """"
    collects smulweb recipe listing pages, extracts html content for listed recipes and saves listing page in file
    page_nr refers to the number trailing smulwebs URL, e.g. 9863 for https://www.smulweb.nl/recepten?page=9863
    Newly published recipes on smulweb appear on incrementing page_nrs, i.e. 9864 will contain newer recipes than 9863
    """

    if SmulWebPage.objects.filter(page_nr=page_nr).exists():
        print(f" Page {page_nr} is already in database.")
          
    else:   
        page_url = 'https://www.smulweb.nl/recepten?page=' + str(page_nr)
        SmulWebPage.objects.create(page_url =page_url, page_nr=page_nr)
        smulwebpage_html = requests.get(page_url).text
        print(f"Collecting page {page_nr}")
        return smulwebpage_html, page_url
        

def extract_recipe_urls(smulwebpage_html, page_url):
    soup = BeautifulSoup(smulwebpage_html, 'html.parser')
    
    urls, recipe_urls = [], []
    regexp = re.compile(r'https://www.smulweb.nl/recepten/[0-9]')

    for a in soup.find_all('a', href = True):  # Get URLs from a tags (which include duplicates of  recipes, users
        if a['href'] not in urls:   # to eliminate duplicate URLs
            urls.append(a['href'])  # save link in urls if not already
    for url in urls:
        if regexp.search(url):  # which selects recipes to save (and leaves out e.g.https://www.smulweb.nl/recepten/nieuw  )
            recipe_urls.append(url)
            print(url)

    print(f"Extracting URLs {recipe_urls} finished")
    return recipe_urls



def scrape_recipes(recipe_urls, page_url):
    """
    This function downloads detailed recipes as listed in a csv file,
    and saves these as individual files in html format, in a directory corresponding with smulweb web page nr for
    recipe listing.
    """

    for recipe_url in recipe_urls:
        r = requests.get(recipe_url)
        recipe_text = r.text
        soup = BeautifulSoup(r.text, "html.parser")
        recipe_data =soup.find("script", {"type":"application/ld+json"}).text
        recipe_json = json.loads(recipe_data)

        print(f"Scraping recipe {recipe_url} from page {page_nr}")
        p = SmulWebPage.objects.get(page_url=page_url)
        s = SmulWebRecipe(recipe_url = recipe_url, recipe_JSON = recipe_json, page_url = p)
        s.save()
        print(f"Saved recipe {recipe_url}")





for page_nr in range(1, 2):
    smulwebpage_html, page_url = get_smulwebpage(page_nr)
    # extracted_recipes = extract_recipe_urls(smulwebpage_html, page_url)
    # scrape_recipes(extracted_recipes, page_url)