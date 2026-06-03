import requests
from bs4 import BeautifulSoup

def get_website_content(url):
    try:
        html = requests.get(url, timeout=10).text
        soup = BeautifulSoup(html, "html.parser")

        text = soup.get_text(separator=" ", strip=True)

        return text[:5000]

    except Exception as e:
        return f"Error: {e}"