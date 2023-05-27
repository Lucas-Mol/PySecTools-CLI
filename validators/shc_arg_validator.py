import sys
from model.security_header_checker import SecurityHeaderChecker

def validate(args):
    try:
        url = args[args.index('-url') + 1]
    except (ValueError, IndexError):
        print('\'-url\' was not passed on args')
        sys.exit()
    
    return SecurityHeaderChecker(url)