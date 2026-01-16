import sys
from crawl import (
    get_html
)

def main():

    argc = len(sys.argv)
    if argc < 2:
        print("no website provided")
        sys.exit(1)
    elif argc > 2:
        print("too many arguments provided")
        #print(sys.argv)
        sys.exit(1)
    
    base_url = sys.argv[1]
    print("starting crawl for: ", base_url)

    try:
        site = get_html(base_url)
        print(site)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
