import sys
from model.ftp_login_brute_force import FTPLoginBruteForce

def validate(args):
    try:
        host = args[args.index('-d') + 1]
    except (ValueError, IndexError):
        print('\'-d\' was not passed on args')
        sys.exit()
    try:
        username = args[args.index('-u') + 1]
    except (ValueError, IndexError):
        print('\'-u\' was not passed on args')
        sys.exit()
    try:
        password_wordlist = args[args.index('-w') + 1]
    except (ValueError, IndexError):
        print('\'-w\' was not passed on args')
        sys.exit()
    
    return FTPLoginBruteForce(host, username, password_wordlist)