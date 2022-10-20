# tlf_liste = [['jens', 12345678, 'medlem'], ['ida', 87853584, 'uberboss']]


# d = {}
# d[1] = ['jens', 12345678, 'medlem']

# d[0] = ['ida', 87853584, 'uberboss']

# print(d)

# print(d[1])


# dict = {}
# dict['espen'] = 45
# dict['pia'] = 25
# dict['bernt'] = 12


# # print(dict.get('pia', 0))
# # print(dict.get('oskar', 0))

# print(dict.keys())

# for key in dict.keys():
#     print(key, dict[key])

# print()
# for k, v in dict.items():
#     print(k, v)


import random


def count_words(streng):
    dict = {}
    streng = streng.split()
    for ord in streng:
        if ord in dict:
            dict[ord] += 1
        else:
            dict[ord] = 1
    return dict


print(count_words('hvis det går fint så går det fint'))
