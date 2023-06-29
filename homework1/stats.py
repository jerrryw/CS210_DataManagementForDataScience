import math

def read():
    list = []
    while True:
        val = int(input())
        if val == -12345:
            break
        list.append(val)
    return list

def mean(list):
    return sum(list) / len(list)

def median(list):
    median = 0
    list.sort()
    length = len(list)
    if (length % 2 == 0):
        median = (list[(length // 2) - 1] + list[(length // 2)]) / 2
    else:
        median = list[(length // 2)]
    return int(median)

def stdev(list):
    mean_val = mean(list)
    val  = 0
    temp = 0
    for i in range(len(list)):
        temp = list[i] - mean_val
        temp = math.pow(temp, 2)
        # print("temp = ", temp)
        val += temp
        # print("val = ", val)
    val = math.sqrt(val * (1 / (len(list) - 1)))
    return val

def stats(list):
    mean_val   = mean(list)
    median_val = median(list)
    stdev_val  = stdev(list)
    print("mean:"              , mean_val)
    print("median:"            , median_val)
    print("standard deviation:", stdev_val)

if __name__ == "__main__":
    list = read()
    stats(list)