#!/usr/bin/python3

ascii_value_of_a = ord('a')

for i in range(26):
    current_char = chr(ascii_value_of_a + i)
    if current_char != 'q' and current_char != 'e':
        print(f"{current_char}", end='')
