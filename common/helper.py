import sys

def run(args):
    print(" -------------------------------------------------------- ")
    print(" ----------------------- Help --------------------------- ")
    print(" -------------------------------------------------------- ")
    print("- PySecTools commands: ")
    print("")
    print("-hbg: HTTP Banner Grabber            Description: Tool to discover the Server OS used by site")
    print("")   
    print("-tps: TCP Port Scanner               Description: Tool to discover the Open ports on Ip target")
    print("")   
    print("-ss: Subdomain Scanner               Description: Tool to discover the available Subdomains based on wordlist")
    print("")   
    print("-ws: Web Scrapper                    Description: Tool to discover and filter links by site")
    print("")   
    print("-shc: Security Header Checker        Description: Tool to discover a missing Security Headers on URL")
    print("")
    print("-lns: Local Network Scanner          Description: Tool to discover devices in your LAN")
    print("")
    print("-wfd: Web File Discovery             Description: Tool to discover files and folders in domain target based on wordlist")
    print("")
    print("-md5c: MD5 Cracker                   Description: Tool to crack a target md5 hash based on wordlist")
    print("")
    print("-ftplbf: FTP Login Brute Force       Description: Tool to attempt a brute force login attack on FTP server based on wordlist")
    print("")
    print("-wd: Wifi Deauth                     Description: Tool to deauth all devices on a wifi network")
    print("")

    sys.exit()

def tps_helper():
    print(" -------------------------------------------------------- ")
    print(" ----------------------- Help --------------------------- ")
    print(" -------------------------------------------------------- ")
    print("- TCP Port Scanner arguments: ")
    print("")
    print("-t: IP target.       REQUIRED!")
    print("")
    print("-s: Start port.      REQUIRED!")
    print("")
    print("-e: End port.        REQUIRED!")
    print("")

    sys.exit()

def hbg_helper():
    print(" -------------------------------------------------------- ")
    print(" ----------------------- Help --------------------------- ")
    print(" -------------------------------------------------------- ")
    print("- HTTP Banner Grabber arguments: ")
    print("")
    print("-url: URL target.    REQUIRED!")
    print("")

    sys.exit()

def ss_helper():
    print(" -------------------------------------------------------- ")
    print(" ----------------------- Help --------------------------- ")
    print(" -------------------------------------------------------- ")
    print("- Subdomain Scanner arguments: ")
    print("")
    print("-d: Domain target.(just domain part of uri)      REQUIRED!")
    print("")
    print("-w: Wordlist path.                               REQUIRED!")
    print("")

    sys.exit()

def ws_helper():
    print(" -------------------------------------------------------- ")
    print(" ----------------------- Help --------------------------- ")
    print(" -------------------------------------------------------- ")
    print("- Web Scrapper arguments: ")
    print("")
    print("-s: Site target.      REQUIRED!")
    print("")

    sys.exit()

def shc_helper():
    print(" -------------------------------------------------------- ")
    print(" ----------------------- Help --------------------------- ")
    print(" -------------------------------------------------------- ")
    print("- Security Header Checker: ")
    print("")
    print("-url: URL target.      REQUIRED!")
    print("")

    sys.exit()

def lns_helper():
    print(" -------------------------------------------------------- ")
    print(" ----------------------- Help --------------------------- ")
    print(" -------------------------------------------------------- ")
    print("- Local Network Scanner arguments: ")
    print("")
    print("-ir: IP range.           REQUIRED!")
    print("")
    print("-int: Network Interface. REQUIRED!")
    print("")

    sys.exit()

def wfd_helper():
    print(" -------------------------------------------------------- ")
    print(" ----------------------- Help --------------------------- ")
    print(" -------------------------------------------------------- ")
    print("- Web File Discovery arguments: ")
    print("")
    print("-d: Domain target.       REQUIRED!")
    print("")
    print("-w: Wordlist path.      REQUIRED!")
    print("")

    sys.exit()

def md5c_helper():
    print(" -------------------------------------------------------- ")
    print(" ----------------------- Help --------------------------- ")
    print(" -------------------------------------------------------- ")
    print("- MD5 Cracker arguments: ")
    print("")
    print("-w: Wordlist path.       REQUIRED!")
    print("")
    print("-t: Target hash.         REQUIRED!")
    print("")

    sys.exit()

def ftplbf_helper():
    print(" -------------------------------------------------------- ")
    print(" ----------------------- Help --------------------------- ")
    print(" -------------------------------------------------------- ")
    print("- FTP Login Brute Force arguments: ")
    print("")
    print("-d: Domain host.             REQUIRED!")
    print("")
    print("-u: Username.                REQUIRED!")
    print("")
    print("-w: Password wordlist path.  REQUIRED!")
    print("")

    sys.exit()

def wd_helper():
    print(" -------------------------------------------------------- ")
    print(" ----------------------- Help --------------------------- ")
    print(" -------------------------------------------------------- ")
    print("- FTP Login Brute Force arguments: ")
    print("")
    print("-i: Interface.             OPTIONAL!")
    print("")

    sys.exit()
