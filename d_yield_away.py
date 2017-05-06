from __future__ import print_function


def classic_fibonacci(limit):
    nums = []
    current, nxt = 0, 1

    while current < limit:
        current, nxt = nxt, nxt + current
        nums.append(current)

    return nums


# fib via generators
def genrator_fib():
    current, nxt = 0, 1

    while True:
        current, nxt = nxt, nxt + current
        yield current


# generators support composition:
def even_fibonacci():
    for n in genrator_fib():
        if n % 2 == 0:
            yield n


# consume both generator as a pipeline here
def composed_generators():
    for e in even_fibonacci():
        if e % 3 == 0:
            yield e


if __name__ == '__main__':

    print('Classic')
    for m in classic_fibonacci(100):
        print(m, end=', ')
    print()

    print('generator')
    for m in genrator_fib():
        print(m, end=', ')
        if m > 100:
            break
    print()

    print('Composed')
    for m in composed_generators():
        print(m, end=', ')
        if m > 1000000:
            break
    print()
