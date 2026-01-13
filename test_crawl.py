import unittest
from crawl import (
    normalize_url, 
    get_h1_from_html, 
    get_first_paragraph_from_html, 
    get_urls_from_html, 
    get_images_from_html, 
    extract_page_data
)

class TestCrawl(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('index.html', 'r') as f:
            cls.html_content = f.read()

    def test_normalize_url(self):
        input_url = "https://blog.boot.dev/path"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_http(self):
        input_url = "http://blog.boot.dev"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev"
        self.assertEqual(actual, expected)

    def test_get_h1_from_html(self):
        html = """<html><body>
                <h1>Welcome to Boot.dev</h1>
                <main>
                <p>Learn to code by building real projects.</p>
                <p>This is the second paragraph.</p>
                </main>
            </body></html>"""
        actual = get_h1_from_html(html)
        expected = "Welcome to Boot.dev"
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html(self):
        html = """<html><body>
                <h1>Welcome to Boot.dev</h1>
                <main>
                <p>Learn to code by building real projects.</p>
                <p>This is the second paragraph.</p>
                </main>
            </body></html>"""
        actual = get_first_paragraph_from_html(html)
        exptected = "Learn to code by building real projects."
        self.assertEqual(actual, exptected)

    def test_get_h1_from_html_file(self):
        h1 = get_h1_from_html(self.html_content)
        expected_h1 = "Welcome to Boot.dev!"
        self.assertEqual(h1, expected_h1)
    
    def test_get_first_paragraph_from_html_file(self):
        paragraph = get_first_paragraph_from_html(self.html_content)
        expected_paragraph = "Learn to code by building real projects."
        self.assertEqual(paragraph, expected_paragraph)

    def test_get_urls_from_html_absolute(self):
        # test both relative and absolute urls
        absolute_url = "https://blog.boot.dev"
        html_input = """<body>
                    <a href='https://blog.boot.dev'>Go to Boot.dev</a>
                    </body>"""
        actual = get_urls_from_html(html_input, absolute_url)
        expected = ["https://blog.boot.dev"]
        #print(f"Actual url: {actual} - Expected: {expected}")
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_relative(self):
        absolute_url = "https://blog.boot.dev"
        html_input = """<body>
                    <a href='/'>Home</a>
                    <a href='/posts/1'>Post 1</a>
                    </body>"""
        actual = get_urls_from_html(html_input, absolute_url)
        expected = ["https://blog.boot.dev/", "https://blog.boot.dev/posts/1"]
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_file(self):
        absolute_url = "https://blog.boot.dev"
        actual = get_urls_from_html(self.html_content, absolute_url)
        expected = ["https://blog.boot.dev", "https://blog.boot.dev/page1"]
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_both(self):
        absolute_url = "https://blog.boot.dev"
        html_input = """<body>
                    <a href='/images/meme.png'>Home</a>
                    <a href='https://blog.boot.dev/posts/1'>Post 1</a>
                    </body>"""
        actual = get_urls_from_html(html_input, absolute_url)
        expected = ["https://blog.boot.dev/images/meme.png", "https://blog.boot.dev/posts/1"]
        self.assertEqual(actual, expected)

    def test_get_images_from_html_absolute(self):
        absolute_url = "https://blog.boot.dev"
        html_input = """<body>
                    <img src='https://blog.boot.dev/images/meme.png'>Home</img>
                    </body>"""
        actual = get_images_from_html(html_input, absolute_url)
        expected = ["https://blog.boot.dev/images/meme.png"]
        self.assertEqual(actual, expected)
    
    def test_get_images_from_html_relative_multiple(self):
        absolute_url = "https://blog.boot.dev"
        html_input = """<body>
                    <img src="/logo2.png" alt="Boot.dev Logo"/>
                    <a href='/posts/2'>Go to Boot.dev</a>
                    <img src="/logo.png" alt="Logo">
                    </body>"""
        actual = get_images_from_html(html_input, absolute_url)
        expected = ["https://blog.boot.dev/logo2.png", "https://blog.boot.dev/logo.png"]
        self.assertEqual(actual, expected)
    
    def test_get_images_from_html_file(self):
        absolute_url = "https://blog.boot.dev"
        actual = get_images_from_html(self.html_content, absolute_url)
        expected = ["https://blog.boot.dev/logo.png", "https://blog.boot.dev/logo2.png"]
        self.assertEqual(actual, expected)

    def test_extract_page_data(self):
        page_url = "https://blog.boot.dev"
        input_html = """<body>
                    <h1>Hello, World</h1>
                    <p>This is my first website</p>
                    <a href='/images/meme.png'>Home</a>
                    <a href='https://blog.boot.dev/posts/1'>Post 1</a>
                    <img src="/images/logo.png">
                    </body>"""
        actual = extract_page_data(input_html, page_url)
        expected = {'url': 'https://blog.boot.dev', 'h1': 'Hello, World', 'first_paragraph': 'This is my first website', 'outgoing_links': ['https://blog.boot.dev/images/meme.png', 'https://blog.boot.dev/posts/1'], 'image_urls': ['https://blog.boot.dev/images/logo.png']}
        
        self.assertEqual(actual, expected)

    def test_extract_page_data_html_file(self):
        page_url = 'https://blog.boot.dev'
        #input_html = self.html_content
        actual = extract_page_data(self.html_content, page_url)
        expected = {'url': 'https://blog.boot.dev', 'h1': 'Welcome to Boot.dev!', 'first_paragraph': 'Learn to code by building real projects.', 'outgoing_links': ['https://blog.boot.dev', 'https://blog.boot.dev/page1'], 'image_urls': ['https://blog.boot.dev/logo.png', 'https://blog.boot.dev/logo2.png']}
        
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()