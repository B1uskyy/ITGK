import random

l = [random.randint(0, 100) for x in range(100)]

# antall = 0

# def plassnummer(liste, tall);
# for i in range(len(liste)):


# for i in range(len(l)):    # 100 ganger
#     for j in range(len(l)):  # 10 000 ganger
#         for k in range(len(l)):  # 1 000 000 ganger
#             antall += 1

# print(antall)

# liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# def søk(sekvens, element):

#     found = False
#     kompleksitet = 0
#     for i in range(len(sekvens)):
#         kompleksitet += 1
#         if sekvens[i] == element:
#             found = True
#             break

#     print("K:", kompleksitet)
#     return found


# print(søk(liste, 2))


def insertion_sort(list):
    for i in range(1, len(list)):
        j = i
        while j > 0 and list[j] < list[j-1]:
            list[j], list[j-1] = list[j-1], list[j]
            j -= 1
    return list


# print(insertion_sort(l))

def fakultet(n):
    if n == 0:
        return 1
    else:
        return n * fakultet(n-1)


print(fakultet(5))
