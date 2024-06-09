from forex_python.converter import CurrencyRates, CurrencyCodes
from requests.exceptions import ConnectionError

c = CurrencyRates()
codes = CurrencyCodes()

def get_user_input():
    amount = input("Enter the amount: ")
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return get_user_input()

    base = input("Enter the base currency (e.g., USD, EUR): ").upper()
    dest = input("Enter the destination currency (e.g., GBP, JPY): ").upper()

    return amount, base, dest

def convert_currency(amount, base, dest):
    try:
        base_symbol = codes.get_symbol(base)
        dest_symbol = codes.get_symbol(dest)

        # Validate currencies
        if base_symbol is None or dest_symbol is None:
            raise ValueError(f'Invalid currency: {base if base_symbol is None else dest}')

        result = c.convert(base_cur=base, dest_cur=dest, amount=amount)
        result = round(result, 3)

        return result, base_symbol, dest_symbol

    except ConnectionError:
        print('Connection error')
        return None, None, None
    except Exception as e:
        print(e)
        return None, None, None

# Main

amount, base, dest = get_user_input()
result, base_symbol, dest_symbol = convert_currency(amount, base, dest)

if result is not None:
    print(f'{amount} {base_symbol} equals {result} {dest_symbol}')
else:
    print("None")