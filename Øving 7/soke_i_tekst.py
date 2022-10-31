# a)
import re


def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()


# print(read_from_file('Alice_in_wonderland.txt'))


# b)

def remove_symbols(text):

    text = re.sub('\W+', ' ', text)
    text = re.sub('[0-9]', '', text)

    return text.lower()


print(remove_symbols(read_from_file('alice_in_wonderland.txt')))
