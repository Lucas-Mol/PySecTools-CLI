import sys
from model.web_scrapper import WebScrapper

def validate(args):
    try:
        site = args[args.index('-s') + 1]
    except (ValueError, IndexError):
        print('\'-s\' was not passed on args')
        sys.exit()
    
    return WebScrapper(site)