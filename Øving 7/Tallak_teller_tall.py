# a)
def number_of_lines(filename):
    f = open(filename, 'r')
    return (len(f.readlines()))


# print(number_of_lines('numbers.txt'))

# b)

def number_frequency(filename):
    tall = {}
    f = open(filename, 'r')
    for lines in f:
        lines = lines.strip()
        if lines in tall:
            tall[lines] += 1
        else:
            tall[lines] = 1
    return tall


# print(number_frequency('numbers.txt'))

# c)

def number_frequency(filename):
    tall = {}

    f = open(filename, 'r')
    for lines in f:
        lines = lines.strip()
        if lines in tall:
            tall[lines] += 1
        else:
            tall[lines] = 1

    for key, value in tall.items():
        print(f'{key}: {value}')


number_frequency('numbers.txt')
