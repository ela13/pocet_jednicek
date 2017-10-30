
cislo = int(input('zadej cele cislo: '))
# pocet_jednicek = cislo.count('1')
# print('pocet jednicek v cisle {} je {}.'.format(cislo, pocet_jednicek))

def pocet_jednicek(cislo):
    pocet = 0
    #if cislo < 0:
    #    cislo = -cislo
    cislo = abs(cislo)
    while cislo > 0:
        zbytek = cislo % 10
        if zbytek == 1:
            pocet = pocet + 1
        cislo = cislo // 10

    return pocet

pocet = pocet_jednicek(cislo)
print('pocet jednicek v cisle {} je {}.'.format(cislo, pocet))
