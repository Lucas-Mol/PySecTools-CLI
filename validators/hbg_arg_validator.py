import sys
from model.http_banner_grabber import HTTPBannerGrabber

def validate(args):
    try:
        url = args[args.index('-url') + 1]
    except (ValueError, IndexError):
        print('\'-url\' was not passed on args')
        sys.exit()
    
    return HTTPBannerGrabber(url)