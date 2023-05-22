import sys
from validators import arg_validator
from common.function_opts_enum import FunctionOptions
from common import printer

printer.pysectools_ascii_logo()

args = arg_validator.validate(sys.argv[1:])

try:
    functional_arg = args[0]
    function_enum = FunctionOptions.get_by_command(functional_arg)
    function_enum._class.run(args)
except ValueError as err:
    print(err.args[0])
    pass
