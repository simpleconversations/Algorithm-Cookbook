## sieve_of_eratosthenes.py
##
## Written by Matthew Egan
## Written on 18th July 2013
##
## Implements the Sieve of Eratosthenes
## Returns an array of primes below x

def main():
    print sieveOfE(121)

def sieveOfE(x):
    numlist = range(3, x+1, 2)
    counter = 0
    backup = 0
    for num in numlist:
        counter = backup
        if num != 0:
            counter += num
            while counter <= len(numlist)-1:
                numlist[counter] = 0
                counter += num
        else:
            pass
        backup += 1
    return [2] + [x for x in numlist if x]

if __name__ == "__main__": main()