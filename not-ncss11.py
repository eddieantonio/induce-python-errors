"""
These are all my failed attempts to induce ncss11.

Namely: TypeError: Expected positive integer or float
"""


def print_error_message(code):
    try:
        exec(code)
    except Exception as error:
        cls = str(type(error).__name__)
        message = str(error).splitlines()[-1]
    else:
        raise Exception(f"This code should have failed, but didn't: {code}")

    print(f"# {cls}: {message}")
    print(code.strip())
    print()


print_error_message(
    """
from time import sleep
sleep(-1)
"""
)

print_error_message(
    """
from math import sqrt
sqrt(-1)
"""
)

print_error_message(
    """
from math import sqrt
sqrt('1')
"""
)

print_error_message(
    """
from math import log
log(-1)
"""
)

print_error_message(
    """
from math import log
log('1')
"""
)

print_error_message(
    """
from random import randrange
randrange('1', '2')
"""
)

print_error_message(
    """
from decimal import Decimal
Decimal.from_float('1')
"""
)

print("# Basically, everything from turtle fails for internal type errors")
print_error_message(
    """
from turtle import *
delay('a')
"""
)

print_error_message(
    """
from turtle import *
screensize('w1', 'w2')
"""
)

print_error_message(
    """
from turtle import *
forward(None)
"""
)
