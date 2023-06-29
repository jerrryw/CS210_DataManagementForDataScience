import numpy as np

if __name__ == "__main__":
    with open("roster2.dat", "r") as filename:
        file = filename.readlines()

    npArr = np.zeros(4, dtype = {'names': ('name', 'age', 'major', 'gpa'),
                               'formats': ('U50', 'i4', 'U4', 'f8')})
    for i in range(4):
        name, age, major, gpa = file[i].strip().split(',')
        npArr[i] = (name, int(age), major, float(gpa))

    print(np.mean(npArr['gpa']))                           #(a)
    print(np.max(npArr[npArr['major'] == 'CS']['gpa']))    #(b)
    print(np.sum(npArr['gpa'] > 3.5))                      #(c)
    print(np.mean(npArr[npArr['age'] >= 25]['gpa']))       #(d)

    temp      = npArr[npArr['age'] <= 22]
    bestMajor = np.unique(temp['major'])
    avgGpa    = [np.mean(temp[temp['major'] == major]['gpa']) for major in bestMajor]
    print(bestMajor[np.argmax(avgGpa)])                    #(e)