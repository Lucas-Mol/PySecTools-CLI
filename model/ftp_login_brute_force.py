class FTPLoginBruteForce:

    def __init__(self, host, username, password_wordlist):
        self.host = host
        self.username = username
        self.password_wordlist = password_wordlist
