# Dette er en overskift

f = open('lesmeg.py', 'r')
# print(type(f))

try:
    for linje in f.readlines():
        print(linje, end='')  # end='' fjerner linjeskift
    f.close()
except FileNotFoundError:
    print("File not found")
