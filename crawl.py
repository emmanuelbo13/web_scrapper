from urllib.parse import urlparse
from bs4 import BeautifulSoup

def normalize_url(absolute_uri):
    parsed_url = urlparse(absolute_uri)
    netloc = parsed_url.netloc.lower()
    path = parsed_url.path or ''
    query = f"?{parsed_url.query}" if parsed_url.query else ''
    normalized_url = f"{netloc}{path}{query}"
    
    return normalized_url
# manual tests:
test_url = "https://blog.boot.dev/path"
expected_url = "blog.boot.dev/path"
#print(normalize_url(test_url))

# Function to extract elements from html
def get_h1_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h1')
    return title.get_text() if title else None

def get_first_paragraph_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    first_paragraph = soup.find_all('p')[0].get_text()
    return first_paragraph
# manual test:
html_test = "<html><body><h1>Test Title</h1><br><p>Hello world</p><p>Hello You</p></body></html>"
html_test2 = '''<html><body>
                <h1>Welcome to Boot.dev</h1>
                <main>
                <p>Learn to code by building real projects.</p>
                <p>This is the second paragraph.</p>
                </main>
            </body></html>'''

# print(get_h1_from_html(html_test2))
# print(get_first_paragraph_from_html(html_test2))

# Get content from file 

with open('index.html', 'r') as f:
    html_content = f.read()

print(html_content)


# class PageScraper:
#     def __init__(self, html):
#         self.soup = BeautifulSoup(html, 'html.parser')
    
#     def get_h1(self):
#         return self.soup.find('title').get_text()
    
#     def get_first_paragraph(self):
#         return self.soup.find_all('p')[0].get_text()

# # Usage:
# scraper = PageScraper(html_test2)
# print(scraper.get_h1())
# print(scraper.get_first_paragraph())