import requests
from validators import wfd_arg_validator
from common import helper

def run(args):
    
    if '-h' in args:
        helper.wfd_helper()

    wfd = wfd_arg_validator.validate(args)

    print('---------------------------------------------')
    print('---------------- Scanning... ----------------')
    print('---------------------------------------------')

    found_urls = []

    domain = wfd.domain
    wordlist = wfd.wordlist

    with open (wordlist, 'r') as file:
        for line in file:
            directory = line.strip()
            target_url = domain + '/' + directory
            response = requests.get(target_url)
            print(f'Trying {target_url}...')
            if (response.status_code == 200):
                found_urls.append(target_url)
                print(f'Found {target_url}')
            else:
                print(f'Not found {target_url}')


    print('---------------------------------------------')
    print('------------- Scanner Complete --------------')
    print('---------------------------------------------')

    if found_urls:
        print(f'All files/folders found: ')
        for found_url in found_urls:
            print(f'==> : {found_url}')
    else:
        print('No file/folder found')


