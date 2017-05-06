from __future__ import print_function


def main():
    print("Find odd numbers via method:")
    print(find_special_numbers(check_for_odd))
    print()

    print("Find divisible by 6 via lambda:")
    print(find_special_numbers(lambda x: x % 6 == 0))
    print()

    print("Sortedd list of words via lambda: ")
    list_of_words = ['CPython', 'read', 'improvements,', 'issues', 'on', 'comprehensive',
                     'user_facing', 'of', 'other', 'for', 'smaller', 'deprecations', 'including',
                     'and', 'please', 'many', 'list']

    list_of_words.sort(key=lambda x: x.lower())
    print(list_of_words)

    print('Done')


def find_special_numbers(special_selector, limit=10):
    found = []
    n = 0
    while len(found) < limit:
        if special_selector(n):
            found.append(n)
        n += 1
    return found


def check_for_odd(n):
    return n % 2 == 1


if __name__ == '__main__':
    main()
