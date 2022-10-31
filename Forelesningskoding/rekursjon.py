import random

l = [random.randint(0, 100) for x in range(100)]

antall = 0

# def plassnummer(liste, tall);
# for i in range(len(liste)):


for i in range(len(l)):    # 100 ganger
    for j in range(len(l)):  # 10 000 ganger
        for k in range(len(l)):  # 1 000 000 ganger
            antall += 1

print(antall)
