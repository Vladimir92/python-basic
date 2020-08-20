# 1. Square func
from functools import wraps
from itertools import repeat
from time import time


def powers(*args, power=2):
    """
    Function get list of digits, calculates the selected pow of each and return calculated list
    :param args: N integers
    :param power: power to apply
    :return: list of powered integers
    """
    return list(map(pow, args, repeat(power)))


def is_prime(num=1):
    """
    Function checks whether the supplied number is prime
    :param num: digit
    :return: true if number is prime, false otherwise
    """
    if num > 1:
        for val in range(2, num):
            if num % val == 0:
                return False
        return True

    return False


COND_EVEN = "EVEN"
COND_ODD = "ODD"
COND_PRIME = "PRIME"


# 2. Digits func
def val_filter(digits, condition=COND_EVEN):
    """
    Function filters input list of integers under specified condition
    :param digits: list of integers
    :param condition: values: EVEN, ODD, PRIME, specifying integers to find in list
    :return: list of integers after applying filter
    """
    if condition == COND_EVEN:
        return list(filter(lambda value: value % 2 == 0, digits))
    if condition == COND_ODD:
        return list(filter(lambda value: value % 2 != 0, digits))
    if condition == COND_PRIME:
        return list(filter(is_prime, digits))
    return []


def timer_decorator(func):
    """
    Decorator function calculates time required to exec decorated function
    :param func: function to decorate
    :return:
    """

    @wraps(func)
    def wrapped(*args):
        start_time = time()
        res = func(*args)
        print("Exec time:", time() - start_time)
        return res

    return wrapped


def depth_decorator(func):
    """
    Decorator that traces the recursion level of inner function
    :param func: function to trace
    :return:
    """
    func.depth = 0

    @wraps(func)
    def wrapped(*args):
        print("_" * func.depth * 4, "-->fib({})".format(*args))
        func.depth += 1
        res = func(*args)
        func.depth -= 1
        print("_" * func.depth * 4, "<--fib({})".format(*args))
        return res

    return wrapped


@depth_decorator
def fib(val):
    if val == 0:
        return 0
    if val == 1:
        return 1
    return fib(val - 1) + fib(val - 2)


@timer_decorator
def add(a, b):
    print("Add ", a, b)
    res = a + b
    print("Result: ", res)
    return res


print(powers(1, 2, 3, power=3))
print(val_filter([1, 2, 3, 4, 5, 6, 7], COND_PRIME))
print("Adding numbers with func, res:", add(1, 3))
print("Fibs processing result", fib(5))
