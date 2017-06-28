from re import fullmatch
from math import modf
from argparse import ArgumentParser


def data_validation(price):
    if isinstance(price, (str, float)):
        if check_decimal_places(price) is False:
            return get_right_price(price)
        else:
            return ValueError
    elif isinstance(price, int):
        return get_right_price(price)


def check_decimal_places(price):
    if isinstance(price, float):
        price = str(price)
    price = price.replace(',', '.')
    price_list = price.split('.')
    return bool(len(price_list[1]) > 3)



def get_right_price(price):
    if isinstance(price, (int, float)):
        return float(price)

    elif isinstance(price, str):
        if fullmatch('\d*[.,]?\d+', price):
            price = price.replace(',', '.')
            return float(price)
        else:
            return ValueError
    else:
        TypeError


def get_right_fractional(fractional):
    if not fractional:
        return ''
    fractional = '{:.2f}'.format(fractional)
    if not float(fractional) < 1:
        fractional = '.99'
    fractional = fractional.lstrip('0')
    return fractional


def format_price(price):
    valid_price = data_validation(price)
    if valid_price is None:
        return TypeError
    elif valid_price is ValueError:
        return ValueError
    fractional, integer = modf(valid_price)
    if integer < 0:
        return ValueError

    format_prices = '{:,.0f}'.format(integer)
    valid_fractional = get_right_fractional(fractional)
    format_prices = format_prices.replace(',', ' ')
    format_prices = format_prices + valid_fractional

    return format_prices


def parser_command_line():
    parser = ArgumentParser()
    parser.add_argument('-p', '--price', nargs='?',
                        required=True, dest='price',
                        help='Format price in *** *** ***.**')
    options = parser.parse_args()
    return options


if __name__ == '__main__':
    options = parser_command_line()
    price = options.price
    print(format_price(price))