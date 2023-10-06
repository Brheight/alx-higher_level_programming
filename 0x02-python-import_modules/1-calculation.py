#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b= 5
if __name__ == "__main__":
    
    add_result = add(a, b)
    sub_result = sub(a, b)
    mul_result = mul(a, b)
    div_result = div(a, b)

    operations = {
        "add": add_result,
        "sub": sub_result,
        "mul": mul_result,
        "div": div_result
    }

    for operation, result in operations.items():
        print(f"{a} {operation} {b} = {result}")
