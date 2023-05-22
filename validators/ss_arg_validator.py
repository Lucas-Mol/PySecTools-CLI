import sys
from model.subdomain_scanner import SubdomainScanner

def validate(args):
    try:
        domain = args[args.index('-d') + 1]
    except (ValueError, IndexError):
        print('\'-d\' was not passed on args')
        sys.exit()
    try:
        wordlist_path = args[args.index('-w') + 1]
    except (ValueError, IndexError):
        print('\'-w\' was not passed on args')
        sys.exit()
    
    return SubdomainScanner(domain, wordlist_path)