# def teller(nummer=0):
#     print("Nå har vi kommet til: ", nummer)
#     teller(nummer + 1)

# teller()

# def teller2():
#     nummer = 0
#     while True:
#         print("Nå har vi kommet til: ", nummer)
#         nummer += 1

# teller()

# def teller(nummer=0):
#     print("Nå har vi kommet til: ", nummer)
#     if (nummer < 10):
#         teller(nummer + 1)


# teller()

# def liste_sum(liste):
#     if(len(liste)==1):
#         return liste[0] #dersom listen kun har et element er summen vår bare det ene elementet
#     else:
#         return liste[0]+liste_sum(liste[1:]) #ellers tar vi det første elementet og legger til summen av resten av lista

# liste_sum([1,2,3])

# def recursive_sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + recursive_sum(n-1)


# print(recursive_sum(53))

# def merge_sum(liste):

#     midt = len(liste) // 2

#     if len(liste) == 1:
#         return liste[0]
#     else:
#         liste1 = merge_sum(liste[:midt])
#         liste2 = merge_sum(liste[midt:])

#     return liste1 + liste2


# print(merge_sum([1, 2, 3, 4, 5, 6]))


# def find_smallest_element(numbers):

#     for n in range(len(numbers) - 1):
#         if numbers[n] < numbers[n + 1]:
#             return numbers[n]
#         else:
#             if numbers[n] > numbers[n + 1]:
#                 continue

#     return numbers


# print(find_smallest_element([3, 6, 10, 3, 12, 15, 32, 11, 54, 22]))


def binary_search(numbers, element, min, max):

    middle = (min + max) // 2

    if element == numbers[middle]:
        return middle

    else:
        if element > numbers[middle]:
            # Her er nummeret på høyre side
            return binary_search(numbers, element, middle + 1, max)
        else:
            return binary_search(numbers, element, min, middle + 1)


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 0, 8))
