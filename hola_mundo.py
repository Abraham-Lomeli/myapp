import math
import os
import random
import re
import sys
def main():
    if n%2 != 0:
        print("Weird")
    else:
        if n<6:
            print("Not Weird")
        elif n<21:
            print("Weird")
        elif n>20:
            print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    main()