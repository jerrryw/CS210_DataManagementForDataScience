import sys

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("\t# include a filename given as a command-line argument")
        sys.exit(1)

    sentences    = []
    unsortedList = []

    with open(sys.argv[1], 'r') as file:
        sentences = [line.split() for line in file]

    for words in sentences:
        unsortedList += words

    sortedList = sorted(unsortedList, key = str.casefold)

    for i in sortedList:
        print(i)