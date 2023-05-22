class SubdomainScanner:

    def __init__(self, domain, wordlist_path):
        self.domain = domain
        self.wordlist_path = wordlist_path
        self.google_dns_ip = '8.8.8.8'
        self.cloudflare_dns_ip = '1.1.1.1'