# Python error messages

These are a series of minimal-reproducible examples ([reprex][]) that
try to induce the top Python error messages reported in
[Jeffries et al. 2022][].

These error messages come from **Python 3.7.15**. The error messages
will change across different versions of the CPython interpreter.

# Top error messages (Jeffries et al. 2022)

This is the list from the ITiCSE paper. I have added an *origin* column
to state whether I think the error message originates from Python and
its standard library (`stdlib`) or some other source/library (`unknown`).

The **code** is an arbitrary code I have assigned to each error message
category in this corpus. The prefix `ncss` comes from the [NCSS
Challenge]. These error messages were collected from the 2019 edition of
the NCSS challenge. The messages are numbered according to their rank in
the corpus. Note, that _our_ ranks might be different, due to skipping,
e.g., error messages that come from an NCSS-specific library.


| Rank | Occurrences | Code   | Origin  | Message |
|-----:|------------:|--------|---------|---------|
|    1 |       40771 | ncss01 | stdlib  | SyntaxError: invalid syntax  |
|    2 |       14255 | ncss02 | stdlib  | NameError: name --- is not defined  |
|    3 |       11997 | ncss03 | stdlib  | IndentationError: expected an indented block  |
|    4 |        8651 | ncss04 | stdlib  | IndentationError: unexpected indent  |
|    5 |        7529 | ncss05 | stdlib  | SyntaxError: EOL while scanning string literal  |
|    6 |        7193 | ncss06 | stdlib  | TypeError: unsupported operand type(s) for ---: ’---’ and ’---’  |
|    7 |        5369 | ncss07 | stdlib  | SyntaxError: unexpected EOF while parsing  |
|    8 |        3377 | ncss08 | stdlib  | IndentationError: unindent does not match any outer indentation level  |
|    9 |        2054 | ncss09 | stdlib  | TypeError: --- takes --- positional arguments but --- given  |
|   10 |        1505 | ncss10 | stdlib  | SyntaxError: Missing parentheses in call to ’print’  |
|   11 |         907 | ncss11 | unknown | TypeError: Expected positive integer or float  |
|   12 |         868 | ncss12 | stdlib  | ValueError: invalid literal for int() with base 10: ’---’  |
|   13 |         771 | ncss13 | stdlib  | SyntaxError: can’t assign to literal  |
|   14 |         715 | ncss14 | unknown | ValueError: Unknown colour name "---"’  |
|   15 |         653 | ncss15 | stdlib  | TypeError: ’---’ object is not ’---’  |
|   16 |         515 | ncss16 | unknown | TypeError: Expected an RGB triple or string color name  |

Upon personal communication with Jeffries, it appears that some error
messages were reworded for the sake of localizing for the audience of
NCSS (namely, Australian middle-schoolers ).

# Top error messages (Kohn 2022)

This list is based on personal communication with [Tobias Kohn][]. According
to Kohn, this is a "heuristic «ad-hoc» list" of error messages", all
originating from CPython. There is no frequency information associated
with this list, and starred (⭐️) error messages are subjectively
specified as the most prominent.

|      | Code    | Message |
|-----:|---------|---------|
|   ⭐️ |   tk01A | **SyntaxError: invalid syntax** |
|      |   tk01B | SyntaxError: cannot assign to literal |
|      |   tk01C | SyntaxError: 'return' outside function |
|      |   tk01D | SyntaxError: 'break' outside loop |
|      |   tk01E | SyntaxError: duplicate  argument '---' in function definition |
|      |   tk01F | SyntaxError: import * only allowed at module level |
|      |   tk01G | SyntaxError: name '---' is parameter and global  |
|   ⭐️ |   tk02A | **IndentationError: unindent does not match  any outer indentation level** |
|   ⭐️ |   tk02B | **IndentationError: unexpected indent** |
|   ⭐️ |   tk03A | **NameError: name '---' is not defined** |
|   ⭐️ |   tk03B | **UnboundLocalError: local variable '---' referenced before assignment** |
|   ⭐️ |   tk04A | **TypeError: ---() takes --- positional arguments but --- were given** |
|   ⭐️ |   tk04B | **TypeError: ---() missing --- required positional argument: '---'** |
|   ⭐️ |   tk04C | **TypeError: '---' object is not callable** |
|   ⭐️ |   tk04D | **TypeError: unsupported operand type(s) for ---: '---' and '---'** |
|      |   tk04E | TypeError: can only concatenate str (not "---") to str |
|      |   tk04F | TypeError: '---' object cannot be interpreted as an integer |
|      |   tk04G | TypeError: '---' object is not subscriptable |
|      |   tk04H | TypeError: list indices must be integers or slices, not --- |
|      |   tk04I | TypeError: cannot unpack non-iterable int object |
|      |   tk04J | TypeError: must be real number, not --- |
|   ⭐️ |   tk05A | **ImportError: cannot import name '---' from '---' (---)** |
|      |   tk05B | ModuleNotFoundError: No module named 'spam'
|   ⭐️ |   tk06A | **AttributeError: 'int' object has no attribute 'spam'** |
|   ⭐️ |   tk07A | **IndexError: list index out of range** |
|      |   tk08A | KeyError: '---' |
|      |   tk09A | ValueError: math domain error |
|      |   tk09B | ValueError: not enough values to unpack (expected ---, got ---) |
|      |   tk09C | ValueError: too many values to unpack (expected ---) |
|      |   tk10A | ZeroDivisionError: division by zero |
|      |   tk10B | ZeroDivisionError: integer division or modulo by zero |
|      |   tk10C | ZeroDivisionError: float division by zero |

[Jeffries et al. 2022]: https://dl.acm.org/doi/abs/10.1145/3502718.3524809
[NCSS Challenge]: https://grokacademy.org/challenge/
[reprex]: https://community.rstudio.com/t/faq-whats-a-reproducible-example-reprex-and-how-do-i-create-one/5219
[Tobias Kohn]: https://tobiaskohn.ch/
