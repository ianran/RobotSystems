from .utils import *
from .basic import *
from .sim_servo import *
from .sim_pwm import *
from .sim_pin import *
from .sim_adc import *
from .sim_modules import *


def __main__():
    import sys
    from .utils import __PRINT__

    usage = '''
Usage:
    ezblock [option]

Options:
    reset-mcu   Reset MCU on Ezblock
    -h          Show this help text and exit
'''
    option = ""
    if len(sys.argv) <= 1:
        __PRINT__(usage)
        quit()
    elif len(sys.argv) > 1:
        option = sys.argv[1]

    if "-h" == option:
        __PRINT__(usage)
        quit()
    elif option == "reset-mcu":
        __PRINT__("MCU Reset.")
        __reset_mcu__()
    else:
        __PRINT__(usage)
        quit()
