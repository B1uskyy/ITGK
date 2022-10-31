# a)

my_set = set()

for i in range(1, 20, 2):
    my_set.add(i)

print(my_set)

# b)

my_set2 = set()

for i in range(1, 10, 2):
    my_set2.add(i)

print(my_set2)

# c)
my_set3 = my_set - my_set2

# d)


def allUnique(lst):
    set1 = set()
    for i in lst:
        set1.add(i)
    if len(set1) < len(lst):
        return False
    else:
        return True

# e)


def removeDuplicates(lst):
    liste = set()
    for i in lst:
        liste.add(i)
    return liste
