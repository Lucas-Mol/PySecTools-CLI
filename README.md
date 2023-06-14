# PySecTools-CLI
A command line interface to offer some basic CyberSecurity tools

## Intro

The PySecTools-CLI is a project made to centralize some basic CyberSecurity tools on a Command Line Interface.

## Overview

![help overview](https://github.com/Lucas-Mol/PySecTools-CLI/assets/93149981/6e152736-5ffc-4db0-8802-6541402dbfed)

## How to run it?
It must be installed:
- Python 3 +

Libs used:
- Requests
- DNS Python
- BeautifulSoup4
- Manuf
- Scapy

So, if you don't have them installed yet, just run: 
   ```
   pip install requests beautifulsoup4 dnspython manuf scapy
   ```

PySecTools have a complete helper for any command, just use `-h`

**Note:** To use Subdomain Scanner, follow <a href='/wordlist.txt'>wordlist.txt</a> file as template example

**And finally**, run command on project's directory:
```
python pysectools.py
```

**Recommendation:**

You can install pyinstaller with:
```
pip install pyinstaller
```
And use: 
``` 
pyinstaller  pysectools.py
```

It'll convert this project to an executable. Therefore, you can add this new executable as a environment variable on PATH and use it at any place on your terminal 😀

## Tech Stack

- Python
- DNS Python
- BeautifulSoup4
- Manuf
- Scapy
- Basic knowledges on: Cybersecurity, Networks, CLI concepts e OOP essentials
