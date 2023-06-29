import sys
from model.md5_cracker import MD5Cracker

def validate(args):
    try:
        wordlist = args[args.index('-w') + 1]
    except (ValueError, IndexError):
        print('\'-w\' was not passed on args')
        sys.exit()
    try:
        target = args[args.index('-t') + 1]
    except (ValueError, IndexError):
        print('\'-t\' was not passed on args')
        sys.exit()
    
    return MD5Cracker(wordlist, target)