import sys

def factor(input):
    for i in range(2, input + 1):
        while input % i == 0:
            # remove nextline
            print(i, end = " ")
            # floor division
            input //= i

if __name__ == "__main__":
    input = int(sys.argv[1])
    factor(input)