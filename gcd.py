## gdc.py
##
## Written by Matthew Egan
## Written on 20th July 2013
##
## Finds the greatest common denomitator
## Finds returns the highest multiple of both numbers (8, 12) => 4

def gcd(a, b):
    while a:
        a, b = b%a, a
    return b

def main():
    print gcd(10, 3)
    print gcd(8, 12)

main()
