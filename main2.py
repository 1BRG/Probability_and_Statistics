from tarfile import data_filter
import time
import numpy as np
import matplotlib.pyplot as plt


def CodeTestedCorectHasBugs(hasBugProb, falseCorrect, falseWrong, n = 10000):
    wrongCount = 0.0000000000000000000001
    totalCorrectCount = 0
    for i in range(0, n):
        hasBug = (np.random.random() < hasBugProb)
        if(hasBug):
            wrongChoice = (np.random.random() < falseCorrect)
            wrongCount += wrongChoice
            totalCorrectCount += wrongChoice
        else:
            goodChoice = (np.random.random() > falseWrong)
            totalCorrectCount += goodChoice

    print(f"Raspuns Corect {falseCorrect * hasBugProb / (falseCorrect * hasBugProb + (1 - falseWrong) * (1 - hasBugProb)) * 100}%")
    print(f"Probabilitatea sa greseasca, i.e. codul sa aiba bug (hasBugProb: "
          f"{hasBugProb}, falseCorrect: {falseCorrect}, falseWrong: {falseWrong}):  {wrongCount / totalCorrectCount * 100}%")
  #  print("\n\n")

def CodeTestedCorectHasBugsVector(hasBugProb, falseCorrect, falseWrong, n = 10000):
    hasBug = (np.random.random(n) < hasBugProb)
    falseCorrectChoice = (np.random.random(n) < falseCorrect)
    goodWrongChoice = (np.random.random(n) > falseWrong)
    wrongCount = 0.0000000000000000000001
    totalCorrectCount = 0
    for i in range(0, n):
        if (hasBug[i]):
            wrongChoice = falseCorrectChoice[i]
            wrongCount += wrongChoice
            totalCorrectCount += wrongChoice
        else:
            goodChoice = goodWrongChoice[i]
            totalCorrectCount += goodChoice
    print(
        f"Raspuns Corect {falseCorrect * hasBugProb / (falseCorrect * hasBugProb + (1 - falseWrong) * (1 - hasBugProb)) * 100}%")
    print(f"Probabilitatea sa greseasca, i.e. codul sa aiba bug (hasBugProb: "
          f"{hasBugProb}, falseCorrect: {falseCorrect}, falseWrong: {falseWrong}):  {wrongCount / totalCorrectCount * 100}%")
  #  print("\n\n")

def ex1():
    x = time.time()
    CodeTestedCorectHasBugs(75/100, 5/100, 2/100)
    CodeTestedCorectHasBugs(5 / 100, 5 / 100, 2 / 100)
    y = time.time()
    print("\nVectorizare:\n")
    CodeTestedCorectHasBugsVector(75 / 100, 5 / 100, 2 / 100)
    CodeTestedCorectHasBugsVector(5 / 100, 5 / 100, 2 / 100)
    z = time.time()
    print()
    print("Timp executie program ineficient: ", y - x)
    print("Timp executie program eficient: ", z - y)

    print("Imbunatatire program: ", (y - x) / (z - y), "X")

def exp(a, b):
    r = []
    for i in range(0, 4):
        r.append([])
        for j in range(0, 4):
            r[i].append(0)

    for i in range(0, len(a)):
        for j in range(0, (len(b))):
            for p in range(0, len(a)):
                r[i][j] += a[i][p] * b[p][j]
    return r


def numberOfCoinLists(n):
    mat = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1/8, 1/8, 2/8, 4/8]]
    r = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    x = [1, 1/8, 3/16, 1/4]
    while(n):
        if(n % 2 == 1):
            r = exp(r, mat)
        mat = exp(mat, mat)
        n //= 2
    val = x[0] * r[3][0] + x[1] * r[3][1] + x[2] * r[3][2] + x[3] * r[3][3]
    print(val * 100)


def numberOfCoinVector(n):
    t = 0
    it = 10000
    for i in range(0, it):
        v = (np.random.random(n) < 0.5)
        ct = 0
        if (v[1] == 1):
            ct += int(v[1]) + int(v[0])
        for i in range(2, n):
            if (v[i] == 1):
                ct += int(v[i])
                if (ct == 3):
                    t += 1
                    break
            else:
                ct = 0
    print(t/it * 100)

def ex2():
    n = 239042034920940294394029
  #  numberOfCoinVector(n)
    numberOfCoinLists(n - 5)

def goatOrCar(doors):
    it = 1000
    change = 0
    keep = 0
    for i in range(0, it):
        rnd = np.random.random()
        d = (rnd < 1/3) + (rnd > 1/3 & rnd < 2/3) * 2 + (rnd > 2/3) * 3




def ex3():
    goatOrCar(100)

def loterie(spam, lotoSpam, lotoNotSpam, n):
    ct = 0
    total= 0
    for i in range(0, n):
        isSpam = (np.random.random() < spam)
        if(isSpam):
            a = (np.random.random() < lotoSpam)
            ct += a
            total += a
        else:
            isNotSpam = (np.random.random() < lotoNotSpam)
            total += isNotSpam
    print(ct / total * 100)

def ex4():
    loterie(30/100, 80/100, 5/100, 10000)
def lab():
    #ex1()
    ex2()
    ex3()
    ex4()



lab()