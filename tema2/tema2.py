def suma_nr(*args, **kwargs):
    s = 0
    for i in args:
        if isinstance(i, int) is True or isinstance(i, float) is True:
            s += i
    return s


suma1 = suma_nr(1, 5, -3, 'abc', [12, 56, 'cad'])
suma2 = suma_nr()
suma3 = suma_nr(2, 4, 'abc', param_1=2)

print(f'Suma1 este : {suma1}')
print(f'Suma2 este : {suma2}')
print(f'Suma3 este : {suma3}')


def functie():
    x = input('Introduceti o valoare: ')
    x =int(x)
    if isinstance(x, int) is True:
        return x
    else:
        return 0


variabila = functie()
if variabila == 0:
    print(f'Variabila nu este nr intreg ({variabila})')
else:
    print(f'Variabila este nr intreg ({variabila})')

import mymodule

x = input('Introduceti un nr: ')
x = int(x)
prim_1 = mymodule.functie_1(x)
print(f'Suma nr pana la {x} este : {prim_1}')


prim_2 = mymodule.functie_2(x)
print(f'Suma nr pare pana la {x} este : {prim_2}')

prim_3 = mymodule.functie_3(x)
print(f'Suma nr impare pana la {x} este : {prim_3}')