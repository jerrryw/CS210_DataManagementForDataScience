import sys
import math

def isPrime(input):
    if input < 1:
        return False
    for i in range(2, (int(math.sqrt(input)) + 1)):
        if input % i == 0:
            return False
    return True

def primes(input):
    for i in range(2, input):
        if isPrime(i):
            # remove nextline
            print(i, end = " ")

if __name__ == "__main__":
    input = int(sys.argv[1])
    primes(input)