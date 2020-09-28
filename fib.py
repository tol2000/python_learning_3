def fib_list(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    import sys
    args = sys.argv[1:]
    print(f"Params: {sys.argv[1:]}")
    a, b = 6, 6
    if len(args) == 2:
        if not(args[0].isdigit() and args[1].isdigit()):
            print("param values are not valid!\nUsing defaults...")
        else:
            a, b = args
            a = int(a)
            b = int(b)
    else:
        print("params count are not valid!\nUsing defaults...")
    print(a, b)
    print(fib_list(a))
    print(fib(b))


if __name__ == '__main__':
    main()
