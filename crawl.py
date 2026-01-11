from urllib.parse import urlparse
from bs4 import BeautifulSoup

def normalize_url(absolute_uri):
    parsed_url = urlparse(absolute_uri)
    netloc = parsed_url.netloc.lower()
    path = parsed_url.path or ''
    query = f"?{parsed_url.query}" if parsed_url.query else ''
    normalized_url = f"{netloc}{path}{query}"
    
    return normalized_url

def get_h1_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h1')
    return title.get_text() if title else None

def get_first_paragraph_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    first_paragraph = soup.find_all('p')[0].get_text()
    return first_paragraph

