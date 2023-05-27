import requests
from common import helper
from validators import shc_arg_validator

def run(args):
    open_ports = []
    
    if '-h' in args:
        helper.shc_helper()

    shc = shc_arg_validator.validate(args)

    print('---------------------------------------------')
    print('---------------- Checking... ----------------')
    print('---------------------------------------------')

    url = str(shc.url)
    HEADERS_TO_CHECK = [
        'Content-Security-Policy',
        'Strict-Transport-Security',
        'X-Frame-Options',
        'X-XSS-Protection',
        'X-Content-Type-Options',
        'Referrer-Policy',
        'Feature-Policy'
    ]

    response = requests.head(url)
    missing_headers = []

    for header in HEADERS_TO_CHECK:
        if header not in response.headers:
            missing_headers.append(header)
            print(f'Missing Header: {header}!!!')
        else:
            print(f'Header: {header} OK!')

    print('---------------------------------------------')
    print('------------- Checker Complete --------------')
    print('---------------------------------------------')

    print('')
    if missing_headers:
        print(f'{url} is missing following headers:')
        for missing_header in missing_headers:
            print(f'[-] {missing_header}')
    else:
        print(f'[+] {url} is OK')