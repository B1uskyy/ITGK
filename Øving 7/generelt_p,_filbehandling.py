
# a)
def write_to_file(data):
    with open('my_file.txt', 'w') as f:
        f.write(data)


# write_to_file('hallo')


# b)

def read_from_file(filename):
    with open(filename, 'r') as f:
        return f.read()


# print(read_from_file('my_file.txt'))


# c)

def main():
    while True:
        action = input('Do you want to read or write? ')
        if action == 'write':
            data = input('What do you want to write to file? ')
            write_to_file(data)
            print(f'{data} was written to file')
        elif action == 'read':
            print(read_from_file('my_file.txt'))
        elif action == 'done':
            print('You are done.')
            break


main()
