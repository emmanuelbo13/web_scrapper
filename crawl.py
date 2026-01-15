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

def get_images_from_html(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    absolute_urls = []
    images = soup.find_all('img')
    for img in images:
        image_src = img.get('src')
        absolute_url = urljoin(base_url, image_src)
        absolute_urls.append(absolute_url)
    
    return absolute_urls

def extract_page_data(html, page_url):
    # Extract url, h1, first_paragraph, outgoing_links, image_urls
    html_contents = {}
    soup = BeautifulSoup(html, 'html.parser')
    
    html_contents['url'] = page_url
    html_contents['h1'] = get_h1_from_html(html)
    html_contents['first_paragraph'] = get_first_paragraph_from_html(html)
    html_contents['outgoing_links'] = get_urls_from_html(html, page_url)
    html_contents['image_urls'] = get_images_from_html(html, page_url)

    return html_contents

import requests
def get_html(url):
    response = requests.get(url, headers={"User-Agent":"BootCrawler/1.0"})
    response.raise_for_status()

    content_type = response.headers.get("Content-Type", "").split(";")[0]
    if content_type != "text/html":
        raise ValueError(f"Invalid content type {content_type}")
    
    return response.text

site = get_html("https://sdf.dev")
print(site)

    

    