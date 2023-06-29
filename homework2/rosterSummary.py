if __name__ == "__main__":
    with open ("roster1.dat", "r") as filename:
        file = filename.readlines()

    list = {}

    for line in file:
        newLine = line.strip().split(",")
        # names   = newLine[0]
        major   = newLine[1]
        gpa     = float(newLine[2])
        credits = float(newLine[3])

        if (major not in list):
            list[major] = {'gpaScores': 0, 'totalCredits': 0, 'countStudents': 0}
        list[major]['gpaScores']     += gpa
        list[major]['totalCredits']  += credits
        list[major]['countStudents'] += 1
        # print(list[major])

    outFile = []
    for major in list:
        avgGpa     = (list[major]['gpaScores']) / (list[major]['countStudents'])
        avgCredits = (list[major]['totalCredits']) / (list[major]['countStudents'])
        count      = (list[major]['countStudents'])
        outFile.append(f"{major},{avgGpa:.1f},{avgCredits:.1f},{count}")

    with open('roster1.out', 'w') as file:
        writeLine = file.write('major,avgGpa,avgCredits,count\n')
        file.write('\n'.join(outFile))