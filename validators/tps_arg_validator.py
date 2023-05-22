import sys
from model.tcp_port_scanner import TCPPortScanner

def validate(args):
    try:
        target = args[args.index('-t') + 1]
    except (ValueError, IndexError):
        print('\'-t\' was not passed on args')
        sys.exit()
    try:
        start_port = int(args[args.index('-s') + 1])
    except (ValueError, IndexError):
        print('\'-s\' was not passed on args')
        sys.exit()
    try:
        end_port = int(args[args.index('-e') + 1])
    except (ValueError, IndexError):
        print('\'-e\' was not passed on args')
        sys.exit()
    
    return TCPPortScanner(target, start_port, end_port)