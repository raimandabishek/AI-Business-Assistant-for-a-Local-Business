# scraper.py
import requests
from bs4 import BeautifulSoup

def get_website_content(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()