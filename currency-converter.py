import requests
import sys
import errno

def get_list_of_currencies():
    """
    Returns a list of currencies available from the api
    """
    r = requests.get('https://api.exchangeratesapi.io/latest')
    data = r.json()
    list_of_currencies = list(data["rates"].keys())
    list_of_currencies.append(data["base"])
    return list_of_currencies

def convert(amount, base, target):
    """
    Converts amount from base currency to target currency 
    """
    r = requests.get('https://api.exchangeratesapi.io/latest?base={}'.format(base))
    data = r.json()
    rate = data["rates"][target]

    return amount * rate
    
def usage(list_of_currencies):
    """
    Display script usage and available currencies
    """
    print("usage: python3 currency-converter.py <amount> <base_currency> <target_currency>\n")
    print("These are the available currencies:\n")
    for i in range(len(list_of_currencies)):
        if i % 11 == 10:
            print("{}".format(list_of_currencies[i]))
        else:
            print("{}".format(list_of_currencies[i]), end= " ")

if __name__ == "__main__":
    list_of_currencies = get_list_of_currencies()
    if len(sys.argv) != 4:
        usage(list_of_currencies)
    else:
        try:
            amount = int(sys.argv[1])
        except ValueError:
            print("'{}' is not a number".format(sys.argv[1]))
            sys.exit(errno.EPERM)

        base = sys.argv[2]
        target = sys.argv[3]

        if base not in list_of_currencies:
            print("'{}' is not a currency\n".format(sys.argv[2]))
            usage(list_of_currencies)
        elif target not in list_of_currencies:
            print("'{} is not a currency\n".format(sys.argv[3]))
            usage(list_of_currencies)
        else:
            target_amount = convert(amount, base, target)
            print("{}: {}\n{}: {}".format(base, amount, target, target_amount))