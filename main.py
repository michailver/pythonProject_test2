# This is a sample Python script.
from binascii import a2b_qp
from sys import api_version


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#uzduotis 1/2
#1
print(8*4+2)
print(8*(4+2))
print(48/4)
print(3+6*2)
#2
a1=5
a2=10
sum_a=a1+a2
print(f'a1={a1}, a2={a2}, suma:{sum_a}')
#3
a1=5
a2=10
a3=2
# suma
print(f'{a1}+{a2}+{a3}={a1+a2+a3}')
# skirtumas
print(f'{a1}-{a2}-{a3}={a1-a2-a3}')
# sandauga
print(f'{a1}*{a2}*{a3}={a1*a2*a3}')
# dalmo
print(f'{a1}/{a2}/{a3}={a1/a2/a3}')

#if uzduotis (6)
#1
a1=5
a2=10
a3=8

if a1==a2:
    print(f'Taip')
else:
    print(f'Ne')
#2 Ar antras ir trečias skaičiai yra lygūs?
if a2==a3:
    print(f'Taip')
else:
    print(f'Ne')
#3 Ar pirmas skaičius yra didesnis už antrąjį?
if a1 > a2:
    print(f'Taip')
else:
    print(f'Ne')
#4 Ar antras skaičius yra didesnis už dvigubą trečiojo skaičiaus reikšmę (trečias skaičius padaugintas iš 2)?
if a2>a3*2:
    print(f'Taip')
else:
    print(f'Ne')
#5 Ar pirmas skaičius yra lyginis (ar dalinasi iš 2)?
if a1//2 == 0:
    print(f'Taip')
else:
    print(f'Ne')
#6 Ar antras skaičius yra nelyginis (ar nesidalina iš 2)?
if a2%2 != 0:
    print(f'Taip')
else:
    print(f'Ne')
#7 Ar trečias skaičius yra teigiamas (didesnis už 0)?
if a2>0:
    print(f'Taip')
else:
    print(f'Ne')
#8 Ar pirmas skaičius yra neigiamas (mažesnis už 0)?
if a1<0:
    print(f'Taip')
else:
    print(f'Ne')
#9 Ar antras skaičius dalinasi iš 4?
if a1 % 4 ==0:
    print(f'Taip')
else:
    print(f'Ne')
#10 Ar trečias skaičius dalinasi iš 8?
if a3 % 8 == 0:
    print(f'Taip')
else:
    print(f'Ne')

#Liepkite vartotojui suvesti savo amžių. Patikrinkite ar amžius yra didesnis arba lygus 18-ai, jei taip - išveskite "jūs galite balsuoti".
amzius = 24
if amzius > 18:
    print (f"jus galite balsuoti")
else:
    print(f"jus ne galite balsuoti")
'''
#Leiskite vartotojui suvesti norimą kiekį pažymių (pavyzdžiui, jūs
nusimatote 3-is kintamuosius, tai leidžiate padaryti 3 įvedimus). Raskite
šių pažymių vidurkį. Patikrinkite ar vidurkis teigiamas (daugiau arba lygu
5-iems), jei taip - išveskite "vidurkis teigiamas".
'''
vidurkis = (a1+a2+a3)/3
if vidurkis >=5:
    print (f'vidurkis teigiamas')
else:
    print(f'vidurkis neigiamas')

'''
4. Susikurkite skaičiaus kintamąjį arba leiskite šį skaičių įvesti vartotojui.
Atlikite šiuos patikrinimus ir veiksmus:'''
a1=25
#1. Jei skaičius dalinasi iš 5, tuomet išveskite šio skaičiaus daugybos lentelę nuo 1 iki 5.
if a1 % 5 == 0:
    print(f'{a1}*1={a1 * 1}')
    print(f'{a1}*1={a1 * 2}')
    print(f'{a1}*1={a1 * 3}')
    print(f'{a1}*1={a1 * 4}')
    print(f'{a1}*1={a1 * 5}')
#2. Jei skaičius lyginis, tuomet išveskite šį skaičių, jo kvadratą ir jį padalintą iš 2.
if a1 % 2 == 0:
    print(f'a1={a1}')
    print(f"a1 kvadrate:{a1*a1}")
    print(f'a1/2={a1/2}')
#3. Jei skaičius nesidalina iš 7, tuomet susikurkite antrąjį kintamąjį, išveskite šių dviejų skaičiu sumą, skirtumą, sandaugą, dalmenį.
if a1 % 7 != 0:
    a2=7
    # suma
    print(f'{a1}+{a2}={a1 + a2}')
    # skirtumas
    print(f'{a1}-{a2}={a1 - a2}')
    # sandauga
    print(f'{a1}*{a2}={a1 * a2}')
    # dalmo
    print(f'{a1}/{a2}={a1 / a2}')
'''
5. Susikurkite tris skaičių kintamuosius su norimomis reikšmėmis, arba
leiskite šiuos skaičius suvesti vartotojui. Patikrinkite šias sąlygas
(naudojant elif dalis):'''
a1=5
a2=4
a3=8
#1. Ar pirmas skaičius didesnis už antrą?

if a1>a2:
    print(f'{a1}>{a2}')
#2. Ar antras skaičius didesnis už trečią?
elif a2>a3:
    print(f'{a2}>{a3}')
#3. Ar trečias skaičius didesnis už pirmą?
elif a3>a1:
    print(f'{a3}>{a1}')
'''
6. Susikurkite tris skaičių kintamuosius su norimomis reikšmėmis, arba
leiskite šiuos skaičius suvesti vartotojui. Patikrinkite šias sąlygas (naudojant
elif dalis):'''
a1=3
a2=5
a3=5
# 1. Ar pirmi du skaičiai yra lygūs?
if a1 == a2:
    print (f'1: {a1} == {a2}')
# 2. Ar paskutiniai du skaičiai yra lygūs?
elif a2 == a3:
    print(f'2: {a2} == {a3}')
# 3. Ar pirmas skaičius yra lygus 0?
elif a1 == 0:
    print(f'3: {a1} == 0')
# 4. Ar antras skaičius neigiamas?
elif a2 < 0:
    print(f'4: {a2} neigiamas')
# 5. Ar trečias skaičius teigiamas?
elif a3 > 0:
    print(f'4: {a2} neigiamas')

'''
7. Susikurkite kintamąjį egzamino pažymiui saugoti [0-10]. Naudojant elif
dalis patikrinkite šias sąlygas ir išveskite atitinkamą tekstą:'''
p = 10
# 1. Jei pažymys yra lygus 10 išvesti “puiku”.
if p == 10:
  print('puiku')
# 2. Jei pažymys yra lygus arba didesnis nei 9 išvesti “labai gerai”.
elif p>=9:
  print('labai gerai')
# 3. Jei pažymys yra lygus arba didesnis nei 7 išvesti “gerai”.
elif p >= 7:
    print ('gerai')
# 4. Jei pažymys yra lygus arba didesnis nei 5 išvesti “patenkinamai”.
elif p >= 5:
    print('patenkinamai')
# 5. Jei pažymys mažesnis nei 5 išvesti “egzaminas neišlaikytas”.
elif p < 5:
    print('egzaminas neišlaikytas')


git config --global user.email "ver.michail@gmail.com"
git config --global user.name "michailver"