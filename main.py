# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from fib import fib_list
from fib import fib_bad


def gen_fac(n):
    x = 1
    res = 1
    while x <= n:
        res = res * x
        yield res
        x += 1


def fac(n):
    res = 0
    if n >= 2:
        x = 1
        g = gen_fac(n)
        while x <= n:
            res = next(g)
            x += 1
    elif n == 1:
        res = 1
    return res


print('Hi!)')

print(f"main fib_list: {fib_list(11)}")
print(f"main fib_bad: {fib_bad(6)}")

gn = 100
f = fac(gn)
print(f"factorial({gn}) == {f}, result length == {len(str(f))}")
