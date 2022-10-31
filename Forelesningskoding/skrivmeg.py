# tall = []

# for i in range(10):
#     tall.append(str(i*i) + '\n')

# # with open('tallene.txt', "w") as f:
# #     for verdi in tall:
# #         f.write(str(verdi) + '\n')


# with open('tallene.txt', 'w') as f:
#     f.writelines(tall)


# Oppgave les_tall_fil.py

import random

f = open('100_tall.txt', 'w')  # åpner filen for skriving
for i in range(100):
    f.write(str(random.randint(1, 100)) + '\n')

f.close()


try:
    f = input("Skriv inn filnavn: ")
    f = open(f, 'r')
    for i in f:
        i = int(i)
        print(f' {i} i tredje er {i**3}')

except FileNotFoundError:
    print("Filen finnes ikke")




# dump av dictiomaries

import pickle # Importerer pickle bibliotek


print('Skriv inn navn, telefon og adresse. Avslutt ENTER')


tlf={} # Oppretter tom dictionary


whileTrue:

    navn = input('Navn: ')

    if(navn==''):

        break # Hopper ut av while-løkka

    telefon = input('Telefonnr: ')

    adresse = input('Adresse: ')

    tlf[navn]=[telefon,adresse]


filnavn = input('Skriv navn på fila: ')

f = open(filnavn,'wb') # Åpner fila for skriving, binær

pickle.dump(tlf,f) # Dumper tlf til disk

f.close() # Stenger fila
