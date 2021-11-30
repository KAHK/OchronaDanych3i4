# Napisz program WyborKluczy, który – wykorzystując rozszerzony algorytm Euklidesa –
# w oparciu o dwie liczby losowe „p” i
# „q”, pozwoli na wygenerowanie pary kluczy: Prywatnego {e, n} i Publicznego {d, n}, takich że:
# +1. Liczba „e” będzie losowa,
# +2. Liczba „e” i (p-1)*(q-1) będą względnie pierwsze,
# 3. Liczba „d” będzie odwrotna do „e” modulo (p-1)*(q-1), czyli e*d = 1 mod (p-1)*(q-1),
# 4. Liczba „n” będzie równała się multiplicationowi „p” i „q”, czyli n = p*q.
# Program musi:
# • wykonywać obliczenia dla liczb „p” i „q” o wielkości do 109, tak żeby „n” mogło wynosić nawet 1018,
# • wyświetlać wygenerowane pary kluczy i zapisywać je w plikach o nazwach – odpowiednio – „public.key” i
# „private.key” (liczby muszą znajdować się w oddzielnych wierszach).
from itertools import takewhile, count
from typing import Set, List
from numpy import random

limit = 10**9


def is_relatively_prime(x, y):
    r: int = None
    while r != 0:
        r = x % y
        x = y
        y = r
    if x == 1:
        return True
    else:
        return False


def get_two_powers(number: int) -> List[int]:
    res = []
    bin_repr = str(bin(number)).partition('b')[2]
    for i, digit in enumerate(reversed(bin_repr)):
        if digit == '1':
            res.append(2 ** i)
    return res


def calculate_power(base: int, mod: int, exponent_two_powers: List[int], exponent_two_powers_set: Set[int]) -> int:
    result = 1
    previous = base % mod
    if 1 in exponent_two_powers_set:
        result *= previous
    for power in takewhile(lambda x: x <= exponent_two_powers[-1], (2 ** x for x in count(1))):
        previous = (previous * previous) % mod
        if power in exponent_two_powers_set:
            result = (result * previous) % mod
    return result


def mod_pow(base: int, exponent: int, *, mod: int) -> int:
    two_powers_list = get_two_powers(exponent)
    two_powers_set = set(two_powers_list)
    res = calculate_power(base, mod, two_powers_list, two_powers_set)
    return res


# liczenie modular_inverse a modulo b
def modular_inverse(a, b):
    gprev = b
    g = a
    vprev = 0
    v = 1
    i = 1
    while g != 0:
        y = gprev/g
        gnext = gprev - y*g
        gprev = g
        g = gnext
        vnext = vprev - y*v
        vprev = v
        v = vnext
        i += 1
    c = vprev

    if c >= 0:
        inv_a = c
    else:
        inv_a = c + b
    nwd = gprev
    if nwd == 1:
        return inv_a


modular_inverseFlag = False
while modular_inverseFlag is False:
    p = random.randint(0, limit)
    q = random.randint(0, limit)
    primalityFlag = False
    while primalityFlag is False:
        e = random.randint(0, limit)
        primalityFlag = is_relatively_prime(e, (p-1)*(q-1))
    d = mod_pow(e, 1, mod=(p-1)*(q-1))
    if d is not None:
        modular_inverseFlag = True


n = p * q

public_key = "e: " + str(e) + "\nn: " + str(n)
private_key = "d: " + str(d) + "\nn: " + str(n)

public_key_file = open("public_key.txt", "w")
public_key_file.write(public_key)
private_key_file = open("private_key.txt", "w")
private_key_file.write(private_key)
