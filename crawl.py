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

def get_urls_from_html(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    anchor_elements = soup.find_all('a')
    return [anchor_elements]

with open('index.html', 'r') as f:
    html_content = f.read()

absolute_url = "https://blog.boot.dev"
relative_url = "/posts/1"

soup = BeautifulSoup(html_content, 'html.parser')
print(soup.find_all('a'))
print(soup.find('a').get('href'))

print(urljoin(absolute_url, relative_url))

def is_absolute(url):
    """Check if a URL is absolute by verifying the scheme and network location."""
    parsed_url = urlparse(url)
    return bool(parsed_url.scheme and parsed_url.netloc)

if is_absolute(relative_url):
    print(relative_url)
else:
    absolute = urljoin(absolute_url, relative_url)