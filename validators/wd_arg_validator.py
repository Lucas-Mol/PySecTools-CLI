import sys
from model.wifi_deauth import WifiDeauth

def validate(args):
    interface = None
    try:
        interface = args[args.index('-i') + 1]
    except (ValueError, IndexError):
        pass
    if interface:
        return WifiDeauth(interface)
    else:
        return WifiDeauth()