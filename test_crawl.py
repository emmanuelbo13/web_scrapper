import unittest
from crawl import normalize_url, get_h1_from_html, get_first_paragraph_from_html, get_urls_from_html

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

    def test_get_urls_from_html(self):
        # test both relative and absolute urls
        absolute_url = "https://blog.boot.dev"
        html_input = """<body>
                    <a href='/posts/1'>Go to Boot.dev</a>
                    <a href='/posts/2'>Go to Boot.dev</a>
                    </body>"""
        actual = get_urls_from_html(html_input, absolute_url)
        expected = ["https://blog.boot.dev/posts/1", "https://blog.boot.dev/posts/2"]
        print(f"Actual url: {actual} - Expected: {expected}")
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()