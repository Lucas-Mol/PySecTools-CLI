import requests
from bs4 import BeautifulSoup
from validators import ws_arg_validator
from common import helper

def run(args):
    
    if '-h' in args:
        helper.ws_helper()

    ws = ws_arg_validator.validate(args)

    print('---------------------------------------------')
    print('---------------- Scrapping... ---------------')
    print('---------------------------------------------')
    urls = set()

    response = requests.get(ws.site)
    soup = BeautifulSoup(response.text, 'html.parser')
    urls = [a['href'] for a in soup.find_all('a', href=True)]

    print('---------------------------------------------')
    print('------------- Scrapper Complete -------------')
    print('---------------------------------------------')
    if urls:
        print('All URLs: ')
        for url in urls:
            print(url)
    else:
        print('No URLs found')
