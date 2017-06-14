# Price Formatter

The script converts the price to the form 0 000 000.00.

The program has two interface:

- Command line interface - run from the console
- Software interface - to work in the program.

and `tests.py` unittest checking the correct operation of the script.


# HowTo
1. Command line interface:

The script requires for it's operation installed Python interpreter version 3.5

```
python format_price.py -p 123456789
123 456 789
```

2. Software interface:

You need to import into the program format_price function.
To write at the beginning of the program code:
```
from format_price import format_price
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
