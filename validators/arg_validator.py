import sys
from common.function_opts_enum import FunctionOptions

def validate(args):

    all_commands = [member.command for member in FunctionOptions]

    if not any(element in args for element in all_commands):
        print('It\'s necessary one functional arg. Use -h to see more.')
        sys.exit()
    
    return args