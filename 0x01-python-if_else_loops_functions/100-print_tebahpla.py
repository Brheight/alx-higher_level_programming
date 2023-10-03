#!/usr/bin/python3

value = ord('z')

is_lowercase = True

while value >= ord('A'):
    if is_lowercase:
        print(chr(value), end="")
    else:
        print(chr(value).upper(), end="")

    is_lowercase = not is_lowercase

    value -= 1

print()
