import requests
from validators import hbg_arg_validator
from common import helper
import sys

def run(args):
    open_ports = []
    
    if '-h' in args:
        helper.hbg_helper()

    hbg = hbg_arg_validator.validate(args)

    print('---------------------------------------------')
    print('---------------- Grabbing... ----------------')
    print('---------------------------------------------')

    url = hbg.url

    response = requests.get(url)

    try:
        server = response.headers['Server']
    except:
        print('Error!')
        sys.exit()

    print('---------------------------------------------')
    print('------------- Grabber Complete --------------')
    print('---------------------------------------------')

    print('')
    print(f'URL: {url}')
    print('')
    print(f'Server: {server}')
