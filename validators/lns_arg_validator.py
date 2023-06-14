import sys
from model.local_network_scanner import LocalNetworkScanner

def validate(args):
    try:
        ir = args[args.index('-ir') + 1]
    except (ValueError, IndexError):
        print('\'-ir\' was not passed on args')
        sys.exit()
    try:
        interface = args[args.index('-int') + 1]
    except (ValueError, IndexError):
        print('\'-int\' was not passed on args')
        sys.exit()
    
    return LocalNetworkScanner(ir, interface)