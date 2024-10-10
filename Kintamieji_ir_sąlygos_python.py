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
# n1 = random.randint(0,4)
# n2 = random.randint(0,4)
# zero=False
# print(f'n1 = {n1}')
# print(f'n2 = {n2}')
# if n1 >= n2:
#     if n2 != 0:
#         result = n1 / n2
#     else:
#         zero=True
# else:
#     if n1 != 0:
#         result = n2 / n1
#     else:
#         zero=True
#
# if zero == False:
#     print(f'Rezultatas: {round(result,2)}')
# else:
#     print(f'ERROR: is nulio nedalinam')
########################################################################################################################
# 3. Naudokite funkcija random.randint(x,x). Sukurkite tris kintamuosius ir naudodamiesi funkcija random.randint(x,x) jiems
# priskirkite atsitiktines reikšmes nuo 0 iki 25. Raskite ir atspausdinkite kintąmąjį turintį vidurinę reikšmę.
n1 = random.randint(0,25)
n2 = random.randint(0,25)
n3 = random.randint(0,25)
errormsg=False

print(f'n1 = {n1}, n2 = {n2}, n3 = {n3},')

small = n1
big = n1
if n2 <= small:
    small = n2
if n3 <= small:
    small = n3
# print(f'small: {small}')

if n2 >= big:
    big = n2
if n3 >= big:
    big = n3
#print(f'big: {big}')

if small < n1 < big:
    midle = n1
elif small < n2 < big:
    midle = n2
elif small < n3 < big:
    midle = n3
else:
    errormsg= True

if not errormsg:
    print(f'midle: {midle}')
else:
    print('Du skaiciai sutampa.')
print('--------')
# print(f'{n1}, {n2}, {n3}')
# print(f'{small}, {midle}, {big}')
########################################################################################################################


