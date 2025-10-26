import time

import numpy as np
import matplotlib.pyplot as plt

def rndIne(n):
    rndList = np.random.random(n)
    for i in range(0, 1):
        prob = []
        cap = 0; pajura = 0
        for i in range(0, n):
            if(rndList[i] < 0.5):
                cap += 1
            else:
                pajura += 1
            prob.append(cap / (i + 1))
        #print("Cap: ", cap, "\nPajura: ", pajura)
       # plt.plot(np.arange(1, n + 1), prob, linewidth = 2, color = "green")

def rndEf(n):
    prob = np.sum(np.random.random(n) < 0.5) / n
    print(prob)

def rndCapPajura(n):
    x = time.time()
    rndIne(n)
    y = time.time()
    rndEf(n)
    z = time.time()

    print("Timp executie program ineficient: ", y - x)
    print("Timp executie program eficient: ", z - y)

    print("Imbunatatire program: ", (y - x) / (z - y), "X")

def dateDeNastere(list, n):
    print("\n\n\nProbabilitati zile nastere:\n")
    for num in list:
        ct = 0
        for i in range(0, n):
            fr = [0] * 380
            for j in range(0, num):
                zi = int(np.random.random() * 365)
                if(fr[zi] != 0):
                    ct += 1
                    break
                fr[zi] = 1
        print("Probabilitate ", num, " persoane: ", ct / n * 100, "%")

def rndEfZaruri(n):
    print("\n\nZaruri Rosu Negru Verde \n")
    rand = np.random.random(n);
    R = 2 * (rand < 1/2) + 5 * (rand > 1/2)
    V = 3 * (rand < 5/6) + 6 * (rand > 5/6)
    N = 4 * (rand < 5/6) + (rand > 5/6)
    rv = 0; rn = 0; vn = 0
    for i in range(0, n):
        if(R[i] > V[i]):
            rv += 1
        if(V[i] > N[i]):
            vn += 1
        if(R[i] > N[i]):
            rn += 1
    print("Rosu bate Verde ", rv / n * 100, "%\nVerde bate Negru ", vn / n * 100, "%\nRosu bate negru ", rn / n * 100, "%\n\n")


plt.style.use('dark_background')
rndCapPajura(1000000)
dateDeNastere([23, 60, 100], 10000)
rndEfZaruri(1000000)


plt.show()

