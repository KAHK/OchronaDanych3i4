#implementacja instrukcji znalezionej tutaj: https://www.gov.pl/web/gov/czym-jest-numer-pesel

wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
pesel = ""


def ostatnia_cyfra_liczby(liczba):
    string_liczba = str(liczba)
    return int(string_liczba[len(string_liczba)-1])


while len(pesel) != 11:
    print("Wpisz numer PESEL:")
    pesel = input()
    if len(pesel) != 11:
        print("PESEL musi składać się z 11 cyfr.")

trimmed_pesel = pesel[:10]

suma_kontrolna = 0

for index in range(0, len(wagi)):
    iloczyn = wagi[index]*int(trimmed_pesel[index])
    suma_kontrolna += ostatnia_cyfra_liczby(iloczyn)

cyfra_kontrolna = 10 - ostatnia_cyfra_liczby(suma_kontrolna)

if cyfra_kontrolna == int(pesel[10]):
    print("PESEL poprawny")
else:
    print("PESEL niepoprawny")
