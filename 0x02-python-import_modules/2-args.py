#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1

    print(f"{argc} {'argument' if argc == 1 else 'arguments'}:", end='')
    if argc > 0:
        print()

    for i in range(1, argc + 1):
        print(f"{i}: {sys.argv[i]}")

