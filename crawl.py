from urllib.parse import urlparse, urljoin
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

def get_urls_from_html(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    absolute_urls = []
    anchor_elements = soup.find_all('a')

    for anchor in anchor_elements:
        anchor_href = anchor.get('href')
        absolute_url = urljoin(base_url, anchor_href)
        absolute_urls.append(absolute_url)

    return absolute_urls

with open('index.html', 'r') as f:
    html_content = f.read()

# manual tests
absolute_url = "https://blog.boot.dev"

print(get_urls_from_html(html_content, absolute_url))
