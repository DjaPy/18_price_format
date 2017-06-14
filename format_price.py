from re import fullmatch
from math import modf
from argparse import ArgumentParser


def get_right_price(price):
    if isinstance(price, (int, float)):
        return float(price)

    if isinstance(price, str):
        if fullmatch('\d*[.,]?\d+', price):
            price = price.replace(',', '.')
            return float(price)
        raise ValueError('An input must match "[0-9].[0-9]" pattern.')
    raise TypeError('An input must be int, float or string matching "[0-9].[0-9]" pattern.')


def get_right_fractional(fractional):
    if not fractional:
        return ''
    fractional = '{:.2f}'.format(fractional)
    if not float(fractional) < 1:
        fractional = '.99'
    fractional = fractional.lstrip('0')
    return fractional


def format_price(price):
    fractional, integer = modf(price)
    print(fractional, integer)
    format_prices = '{:,.0f}'.format(integer)
    valid_fractional = get_right_fractional(fractional)
    format_prices = format_prices.replace(',', ' ')
    format_prices = format_prices + valid_fractional
    return format_prices


def parser_command_line():
    parser = ArgumentParser()
    parser.add_argument('-p', '--price', nargs='?',
                        required=True, dest='price',
                        help='Format price in *** *** ***. **')
    options = parser.parse_args()
    return options


if __name__ == '__main__':
    options = parser_command_line()
    price = options.price
    price = get_right_price(price)
    print(format_price(price))