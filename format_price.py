import argparse
import re
match = re.compile(r'\d+\.?\d*$')


def format_price(price):
    if (isinstance(price, (int, float)) or
            isinstance(price, str) and re.match(match, price)):
        price = float(price)
        if price.is_integer():
            return format(price, ',.0f').replace(',', ' ')
        else:
            return format(price, ',.2f').replace(',', ' ')
    else:
        raise ValueError('Incorrect value')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='returns price in human-readable format')
    parser.add_argument('price', help='input price')
    args = parser.parse_args()
    print(format_price(args.price))
