import sys
from model.web_file_discovery import WebFileDiscovery

def validate(args):
    try:
        domain = args[args.index('-d') + 1]
    except (ValueError, IndexError):
        print('\'-d\' was not passed on args')
        sys.exit()
    try:
        wordlist = args[args.index('-w') + 1]
    except (ValueError, IndexError):
        print('\'-w\' was not passed on args')
        sys.exit()
    
    return WebFileDiscovery(domain, wordlist)