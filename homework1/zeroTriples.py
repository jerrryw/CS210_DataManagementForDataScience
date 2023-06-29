def read():
    list = []
    while True:
        val = int(input())
        if val == -12345:
            break
        list.append(val)
    return list

# [*, *, *, *, *, *]
# [i, j, n, *, *, *]
# [i, j, *, n, *, *]
# [i, j, *, *, n, *]
# [i, j, *, *, *, n]
def zeroTriples(inputs):
    list = []
    for i in range(len(inputs) - 2):
        for j in range(i + 1, len(inputs) - 1):
            for n in range(j + 1, len(inputs)):
                # print("i = ", i, ", inputs[i] = ", inputs[i])
                # print("j = ", j, ", inputs[j] = ", inputs[j])
                # print("n = ", n, ", inputs[n] = ", inputs[n])
                # print("====================================")
                if (inputs[i] + inputs[j] + inputs[n] == 0):
                    list.append((inputs[i], inputs[j], inputs[n]))
    return list

if __name__ == '__main__':
    inputs = read()
    zeros = zeroTriples(inputs)

    if (len(zeros) == 0):
        print("0 triples found")
    else:
        if (len(zeros) == 1):
            print("1 triple found: ")
        else:
            print(len(zeros), "triples found: ")

        for i in zeros:
            # convert from int list to string list
            str_i = str(i)
            # remove parentheses from list
            clean = str_i.replace('(', '').replace(')', '')
            print(clean)