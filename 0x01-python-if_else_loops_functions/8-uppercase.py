#!/usr/bin/python3

def uppercase(input_str):
    result_str = ""

    for char in input_str:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - 32)
            result_str += uppercase_char
        else:
            result_str += char  

    print(result_str)

if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
