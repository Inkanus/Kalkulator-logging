import operator
from functools import reduce
import logging
logging.basicConfig(format='%(level)s - %(message)s', level=logging.DEBUG)

print()
print()

# Dodawanie
def add(*args):
    logging.info(f"Dodawanie {numbers}")
    return reduce(operator.add, args)


# Odejmowanie


def subtract(*args):
    logging.info(f"Odejmowanie {numbers}")
    return reduce(operator.sub, args)


# Mnożenie


def multiply(*args):
    logging.info(f"Mnożenie {numbers}")
    return reduce(operator.mul, args)


# Dzielenie


def divide(*args):
    logging.info(f"Dzielenie {numbers}")
    return reduce(operator.truediv, args)


def get_data():
    choice = input("Wybierz działanie(1/2/3/4): ")
    args = []
    if choice in "1234":
        while True:
            num = input("Podaj kolejną liczbę lub naciśnij q aby wyjść: ")
            if num == 'q':
                break
            args.append(float(num))
    return args, choice


print("Podaj działanie, posługując się odpowiednią liczbą:")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")

operations = {
    '1': add,
    '2': subtract,
    '3': multiply,
    '4': divide,
}

numbers, choice = get_data()
result = operations[choice](*numbers)
print("Wynik:", result)