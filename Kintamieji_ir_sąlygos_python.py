import datetime
import random
from webbrowser import open_new

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
# n1 = random.randint(0,25)
# n2 = random.randint(0,25)
# n3 = random.randint(0,25)
# errormsg=False
#
# print(f'n1 = {n1}, n2 = {n2}, n3 = {n3},')
#
# small = n1
# big = n1
# if n2 <= small:
#     small = n2
# if n3 <= small:
#     small = n3
# # print(f'small: {small}')
#
# if n2 >= big:
#     big = n2
# if n3 >= big:
#     big = n3
# #print(f'big: {big}')
#
# if small < n1 < big:
#     midle = n1
# elif small < n2 < big:
#     midle = n2
# elif small < n3 < big:
#     midle = n3
# else:
#     errormsg= True
#
# if not errormsg:
#     print(f'midle: {midle}')
# else:
#     print('Du skaiciai sutampa.')
# print('--------')
# print(f'{n1}, {n2}, {n3}')
# print(f'{small}, {midle}, {big}')
########################################################################################################################
# Įvedami skaičiai - a, b, c –kraštinių ilgiai, trys kintamieji (naudokite random.randint(x,x) funkciją nuo 1 iki 10).
# Parašykite Python programą, kuri nustatytų, ar galima sudaryti trikampį ir atsakymą atspausdintų.
# a = random.randint(1,10)
# b = random.randint(1,10)
# c = random.randint(1,10)
# if a + b > c and a + c > b and b + c >a:
#     print(f'{a}, {b}, {c}, Trikampis')
# else:
#     print(f'{a}, {b}, {c}, Ne Trikampis')
########################################################################################################################
# 5. Sukurkite keturis kintamuosius ir random.randint(x,x) funkcija sugeneruokite jiems reikšmes nuo 0 iki 2.
# Suskaičiuokite kiek yra nulių, vienetų ir dvejetų. (sprendimui masyvo nenaudoti).
# n1 = random.randint(0,2)
# n2 = random.randint(0,2)
# n3 = random.randint(0,2)
# n4 = random.randint(0,2)
#
# zero = 0
# one = 0
# two = 0
#
# if n1 == 0:
#     zero += 1
# elif n1 == 1:
#     one += 1
# else:
#     two += 1
#
# if n2 == 0:
#     zero += 1
# elif n2 == 1:
#     one += 1
# else:
#     two += 1
#
# if n3 == 0:
#     zero += 1
# elif n3 == 1:
#     one += 1
# else:
#     two += 1
#
# if n4 == 0:
#     zero += 1
# elif n4 == 1:
#     one += 1
# else:
#     two += 1
#
# print(f'{n1, n2, n3, n4}')
# print(f'Nuliu: {zero}')
# print(f'Vienetu: {one}')
# print(f'dviejetu: {two}')
########################################################################################################################
# 6. Naudokite funkcija random.randint(x,x). Sukurkite ir atspausdinkite 3 skaičius nuo -10 iki 10. Skaičiai mažesni už 0
# turi būti  laužtiniuose skliaustuose [], 0 -  (), didesni už 0 {}.   [-4],  (0)
n1 = random.randint(-10,10)
n2 = random.randint(-10,10)
n3 = random.randint(-10,10)

print(f'{n1}, {n2}, {n3}')
answer=''

if n1 == 0:
    answer += f'({n1}),'
elif n1 < 0  :
    answer += f'[{n1}],'
else:
    answer += '{' + f'{n1}' + '},'

if n2 == 0:
    answer += f'({n2}),'
elif n2 < 0  :
    answer += f'[{n2}],'
else:
    answer += '{' + f'{n2}' + '},'

if n3 == 0:
    answer += f'({n3})'
elif n3 < 0  :
    answer += f'[{n3}]'
else:
    answer += '{' + f'{n3}' + '}'

print(answer)

########################################################################################################################
# 7. Įmonė parduoda žvakes po 1 EUR. Perkant daugiau kaip 1000 vienetų taikoma 3 % nuolaida, daugiau kaip 2000 vienetų
# -4% nuolaida. Parašykite programą, kuri skaičiuos žvakių kainą ir atspausdintų atsakymą kiek žvakių ir kokia kaina perkama.
# Žvakių kiekį generuokite ​random.randint(x,x)​ funkcija nuo 5 iki 3000.
import random

price = float(1)
more1000 = 3 #discount
more2000 = 4 #discount
sale_count = random.randint(5,3000)

if 1000 < sale_count <= 2000:
    new_price = price - (price * more1000/100)
elif sale_count > 2000:
    new_price = price - (price * more2000/100)
else:
    new_price = price
print (f'perkama {sale_count} zvakiu, kaina uz vnt {new_price} euru')
# print (new_price)

########################################################################################################################
# 8. Naudokite funkcija random.randint(x,x). Sukurkite tris kintamuosius su atsitiktinėm reikšmėm nuo 0 iki 100.
# Paskaičiuokite jų aritmetinį vidurkį. Ir aritmetinį vidurkį atmetus tas reikšmes, kurios yra mažesnės nei 10
# arba didesnės nei 90. Abu vidurkius atspausdinkite. Rezultatus apvalinkite iki sveiko skaičiaus.
n2 = random.randint(0,100)
n3 = random.randint(0,100)
n1 = random.randint(0,100)
number_count = 0
sum = 0
print(f'{n1}, {n2}, {n3}')
average1 = (n1+n2+n3)/3

if n1>10 and n1<90:
    sum=sum+n1
    number_count+=1
if n2>10 and n2<90:
    sum=sum+n2
    number_count+=1
if n3>10 and n3<90:
    sum=sum+n3
    number_count+=1
print(f'pilnas vidurkis: {round(average1,0)}')
# print(f'sum: {sum}')
# print(f'number_count: {number_count}')

if number_count>0 and number_count!=3:
    average2=sum/number_count
    print(f'Atmestas vidurkis: {round(average2,0)}')
########################################################################################################################
# 9. Padarykite skaitmeninį laikrodį, rodantį valandas, minutes ir sekundes. Valandom, minutėm ir sekundėm sugeneruoti
# panaudokite funkciją random.randint(x,x). Sugeneruokite skaičių nuo 0 iki 300. Tai papildomos sekundės.
# Skaičių pridėkite prie jau sugeneruoto laiko. Atspausdinkite laikrodį prieš ir po sekundžių pridėjimo
# ir pridedamų sekundžių skaičių.
import datetime
import random

h = random.randint(0,23)
m = random.randint(0,59)
s = random.randint(0,59)
add_s = random.randint(0,300)

a = datetime.datetime(2020,6,1,h,m,s)
print(f'Laikrodis Priesh: {a.strftime("%X")}')
print(f'Pridedam {add_s} sekundziu')
b = a + datetime.timedelta(seconds=add_s)
print(f'Laikrodis po: {b.strftime("%X")}')
