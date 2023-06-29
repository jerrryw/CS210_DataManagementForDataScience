import sys

def isIncre(input):
    sVal = str(input)
    for i in range(len(sVal) - 1):
        # print(sVal)
        # print("i    : ", sVal[i])
        # print("i + 1: ", sVal[i + 1])
        if (int(sVal[i])) >= (int(sVal[i + 1])):
            # print("stderr")
            return False
    return True

def count(input):
    count = 0
    for i in range(1, input + 1):
        # print(i)
        if isIncre(i):
            count += 1
    return count

if __name__ == "__main__":
    input = int(sys.argv[1])
    print(count(input))