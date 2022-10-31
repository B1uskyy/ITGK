# Unntak


# try:
#     tall = int(input("Skriv inn et tall: "))
#     print(f"4/{tall} = {4/tall}")    # 0 her gir feil
# except Exception as e:
#     print(f"Noe ble feil, {e}")


# try_except.py

# Kan behandle ulike feiler forskjellig!!


def main():
    try:

        tall = int(input("Skriv inn et tall: "))

        print("500 delt på", tall, "er", 500/tall)

        filnavn = input("Skriv inn et filnavn: ")

        f = open(filnavn)

        tekst = f.read()

        print(tekst)

    except ValueError:

        print("FEIL: Må skrive inn et tall, ikke tekststreng!!!")

    except ZeroDivisionError:

        print("FEIL: Kan ikke skrive tallet 0!!!")

    except IOError:

        print("FEIL: Det oppsto en feil ved lesing av fila", filnavn)

    except:

        print("FEIL: Programmet feilet av uvisst grunn!")


main()


# oppgave_try.py

try:
    tall = int(input("Skriv inn et tall: "))
    tall2 = int(input("Skriv inn et tall til: "))

    print(f"{tall} delt på {tall2} er {tall / tall2}")

except ZeroDivisionError:
    print("Noe galt har skjedd")
except ValueError:
    print("Du må skrive inn et tall")
else:
    # Blir utført hvis ingen exceptions ble trigget
    print("Hvordan blir du med ?")
finally:
    # Blir utført uansett om exceptions ble trigget eller ikke
    print("Dette skjer uansett")
