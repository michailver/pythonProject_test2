import datetime
import random

# Sukurkite 4 kintamuosius, kurie saugotų jūsų vardą, pavardę, gimimo metus ir šiuos metus (nebūtinai tikrus).
# Parašykite kodą, kuris pagal gimimo metus paskaičiuotų jūsų amžių ir naudodamas vardo ir pavardės kintamuosius atspausdintų tokį sakinį :
# "Aš esu Vardenis Pavardenis. Man yra XX metai(ų)".


# name='Michail'
# surname='Vermishel'
# bday=datetime.date(2000,10,10)
# print(f'Aš esu {name} {surname}. Man yra {datetime.date.today().year - bday.year} metai(ų)')
########################################################################################################################
# Sukurkite du kintamuosius ir naudodamiesi funkcija random.randint(x,x) jiems priskirkite atsitiktines reikšmes nuo 0 iki 4.
# Didesnę reikšmę padalinkite iš mažesnės. Atspausdinkite rezultatą jį suapvalinę iki 2 skaičių po kablelio.
n1 = random.randint(0,4)
n2 = random.randint(0,4)
zero=False
print(f'n1 = {n1}')
print(f'n2 = {n2}')
if n1 >= n2:
    if n2 != 0:
        result = n1 / n2
    else:
        zero=True
else:
    if n1 != 0:
        result = n2 / n1
    else:
        zero=True

if zero == False:
    print(f'Rezultatas: {round(result,2)}')
else:
    print(f'ERROR: is nulio nedalinam')