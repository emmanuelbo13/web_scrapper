from urllib.parse import urlparse

def normalize_url(absolute_uri):
    parsed_url = urlparse(absolute_uri)
    netloc = parsed_url.netloc.lower()
    path = parsed_url.path or ''
    query = f"?{parsed_url.query}" if parsed_url.query else ''
    normalized_url = f"{netloc}{path}{query}"
    
    return normalized_url

# --- Manual Test ---
test_url = "https://blog.boot.dev/path"

expected_url = "blog.boot.dev/path"

print(normalize_url(test_url))
