from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

def normalize_url(input_url):
    parsed_url = urlparse(input_url)
    netloc = parsed_url.netloc.lower()
    path = parsed_url.path or ''
    query = f"?{parsed_url.query}" if parsed_url.query else ''
    normalized_url = f"{netloc}{path}{query}"
    
    return normalized_url    

def get_h1_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    h1s = soup.find_all('h1')
    for h1 in h1s:
        h1_text = h1.get_text() if h1 else None
    return h1_text

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

# input_url = "blog.boot.dev"
# scheme = urlparse(input_url).scheme

# if not scheme:
#     print("No scheme - add https://")
#     absolute_url = f"https://{input_url}"
#     print(absolute_url)

# with open('index.html', 'r') as f:
#     html_content = f.read()



def get_images_from_html(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    absolute_urls = []
    images = soup.find_all('img')
    for img in images:
        image_src = img.get('src')
        absolute_url = urljoin(base_url, image_src)
        absolute_urls.append(absolute_url)
    
    return absolute_urls