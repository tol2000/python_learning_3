import logging
from functools import lru_cache


def fib_list(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


fib_calls = 0


@lru_cache(maxsize=1000)
def fib_bad(n, first_call=True):
    global fib_calls
    if first_call:
        fib_calls = 1
    else:
        fib_calls += 1
    if n <= 1:
        return n
    else:
        return fib_bad(n - 1, False) + fib_bad(n - 2, False)


def fib(n, first_call=True):
    global fib_calls
    if first_call:
        fib_calls = 1
    else:
        fib_calls += 1
    if n == 0:
        # tuple(prev, next)
        return 0, 1
    else:
        v_prev, v_next = fib(n - 1, False)
        return v_next, v_prev + v_next


def main():
    import sys
    args = sys.argv[1:]
    logging.info(f"Params: {sys.argv[1:]}")
    a, b = 6, 300
    if len(args) == 2:
        if not(args[0].isdigit() and args[1].isdigit()):
            logging.info(f"param values are not valid! Using defaults: {a, b}")
        else:
            a, b = args
            a = int(a)
            b = int(b)
    else:
        logging.info(f"params count are not valid! Using defaults: {a, b}")

    logging.info(f"fib_list({a}) = {fib_list(a)}")
    logging.info(f"fib({b}) = {fib(b)[0]}, fib calls: {fib_calls}")
    logging.info(f"fib_bad({b}) = {fib_bad(b)}, fib_bad calls: {fib_calls}, fib_bad cache info: {fib_bad.cache_info()}")


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s [LINE:%(lineno)-10d] # %(levelname)-8s [%(asctime)s] %(message)s"
    )
    logging.info("Calling as standalone")
    main()
else:
    print("Importing package...")
