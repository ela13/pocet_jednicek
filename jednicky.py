
cislo = int(input('zadej cele kladne cislo: '))
# pocet_jednicek = cislo.count('1')
# print('pocet jednicek v cisle {} je {}.'.format(cislo, pocet_jednicek))

def pocet_jednicek(cislo):
    cislo = abs(cislo)
    pocet = 0
    while cislo > 0:
        zbytek = cislo % 10
        if zbytek == 1:
            pocet = pocet + 1
        cislo = cislo // 10

    return pocet

pocet = pocet_jednicek(cislo)
print('pocet jednicek v cisle {} je {}.'.format(cislo, pocet))
