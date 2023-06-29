import hashlib
from validators import md5c_arg_validator
from common import helper

def run(args):
    
    if '-h' in args:
        helper.md5c_helper()

    md5c = md5c_arg_validator.validate(args)

    found_password = None

    print('---------------------------------------------')
    print('---------------- Cracking... ----------------')
    print('---------------------------------------------')

    with open(md5c.wordlist, 'r') as wordlist_file:
        for password in wordlist_file:
            print(f'Trying password: {password} ...')
            password = password.strip()
            hash_guess = get_md5_hash(password)
            if hash_guess == md5c.taget:
                found_password = password

    print('---------------------------------------------')
    print('------------- Cracker Complete --------------')
    print('---------------------------------------------')

    print('')
    if found_password:
        print(f'Found Password: {found_password}')
    else:
        print('Password not found')


def get_md5_hash(input_string):
    md5_hasher = hashlib.md5()
    md5_hasher.update(input_string.encode('utf-8'))
    hash_string = md5_hasher.hexdigest()
    return hash_string
