import dns.resolver
from validators import ss_arg_validator
from common import helper

def run(args):
    
    if '-h' in args:
        helper.ss_helper()

    ss = ss_arg_validator.validate(args)

    print('---------------------------------------------')
    print('---------------- Scanning... ----------------')
    print('---------------------------------------------')

    subdomains = set()
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [ss.google_dns_ip]

    with open(ss.wordlist_path) as f:
        wordlist = f.read().splitlines()
        for word in wordlist:
            subdomain = f'{word}.{ss.domain}'
            print(f'Trying {subdomain}...')
            try:
                answer = resolver.resolve(subdomain)
                if answer:
                    subdomains.add(subdomain)
                    print(f'Found {subdomain}')
            except:
                print(f'Not found {subdomain}')

    print('---------------------------------------------')
    print('------------- Scanner Complete --------------')
    print('---------------------------------------------')
    if subdomains:
        print(f'All subdomains: ')
        for subdomain in subdomains:
            print(subdomain)
    else:
        print('No subdomains found')
