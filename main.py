import logging
# from fib import fib_list
# from fib import fib_bad
import fib

logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s [LINE:%(lineno)-10d] # %(levelname)-8s [%(asctime)s] %(message)s"
)


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


logging.info('Hi!)')

logging.info(f"main fib_list: {fib.fib_list(11)}")
logging.info(f"main fib_bad: {fib.fib_bad(6)}")

gn = 100
f = fac(gn)
print(f"factorial({gn}) == {f}, result length == {len(str(f))}")
