# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import fib


def genfac(n):
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
        g = genfac(n)
        while x <= n:
            res = next(g)
            x += 1
    elif n == 1:
        res = 1
    return res


print('Hi!)')

print(fib.fib_list(11))
print(fib.fib_bad(6))

n = 10

print(f"factorial({n}) == {fac(n)}")