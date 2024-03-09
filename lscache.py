import logging
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

logging.basicConfig(filename='/home/jazirat1/precache.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def get_sitemap_urls(urls):
    all_urls = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "lxml-xml")
        urls = [loc.text for loc in soup.find_all("loc") if "wp-content/uploads" not in loc.text]
        all_urls.extend(urls)
    return all_urls


chromedriver_path = '/home/jazirat1/chromedriver'

sitemap_urls = [
    'https://jaziratalkanz.ma/page-sitemap.xml',
    'https://jaziratalkanz.ma/post-sitemap.xml',
    'https://jaziratalkanz.ma/category-sitemap.xml',
    'https://jaziratalkanz.ma/author-sitemap.xml',
]

start_time = time.time()

urls = get_sitemap_urls(sitemap_urls)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)



for url in urls:
    if "wp-content/uploads" in url:
        continue
    try:
        logging.info("Mise en cache: %s", url)
        print("Mise en cache:", url)
        driver.get(url)

        time.sleep(1)
    except WebDriverException as e:
        print(f"Echec de mise en cache {url}: {e}")

driver.quit()

elapsed_time = time.time() - start_time
print(f"Temps d'execution: {elapsed_time} secondes")
logging.info(f"Temps d'execution: {elapsed_time} secondes")
