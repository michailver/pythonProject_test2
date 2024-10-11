########################################################################################################################
#1. Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus (Jonas Jonaitis).
# Atspausdinti trumpesnį stringą.
# actor1='Jonas Jonaitis'
# actor2='Petras Petraitis'
# if len(actor1) < len(actor2):
#     print (f'Trumpesnį stringą yra: {actor1}. ilgis {len(actor1)}')
# elif len(actor1) == len(actor2):
#     print(f'stringą vienodo ilgio: {actor1}, {actor2}')
# else:
#     print(f'Trumpesnį stringą yra: {actor2}. ilgis {len(actor2)}')
#

########################################################################################################################
# 2. Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus.
# Vardą atspausdinti tik didžiosiom raidėm, o pavardę tik mažosioms. (LEONARDO dicaprio)
# actor1 = 'Jonas Jonaitis'
# actor2 = 'Petras Petraitis'
# print(actor1.split()[0].upper(), actor1.split()[1].lower())
# print(actor2.split()[0].upper(), actor2.split()[1].lower())

########################################################################################################################
# 3. Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus.
# Sukurti trečią kintamąjį ir jam priskirti stringą, sudarytą iš pirmų vardo ir pavardės kintamųjų raidžių.
# Jį atspausdinti.
# actor1 = 'Jonas Jonaitis'
# actor2 = 'Petras Petraitis'
# first_name1 = actor1.split()[0]
# last_name1 = actor1.split()[1]
# first_name2 = actor2.split()[0]
# last_name2 = actor2.split()[1]
# answer = first_name1[0] + last_name1[0] + first_name2[0] + last_name2[0]
# print(answer)

########################################################################################################################
# 4. Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus.
# Sukurti trečią kintamąjį ir jam priskirti stringą, sudarytą iš trijų paskutinių vardo ir pavardės kintamųjų raidžių.
# Jį atspausdinti.
# actor1 = 'Jonas Jonaitis'
# actor2 = 'Petras Petraitis'
# first_name1 = actor1.split()[0]
# last_name1 = actor1.split()[1]
# first_name2 = actor2.split()[0]
# last_name2 = actor2.split()[1]
# answer1=first_name1[-3:] + last_name1[-3:]+first_name2[-3:]+last_name2[-3:]
# print(answer1)

########################################################################################################################
# 5. Sukurti kintamąjį su stringu: "An American in Paris".
# Jame visas “a” (didžiąsias ir mažąsias) pakeisti žvaigždutėm “*”.  Rezultatą atspausdinti.
# txt = 'An American in Paris'
# result = txt.replace('a','*').replace('A','*')
# print(result)

########################################################################################################################
# 6. Sukurti kintamąjį su stringu: "An American in Paris". Jame ištrinti visas balses. Rezultatą atspausdinti.
# Kodą pakartoti su stringais: "Breakfast at Tiffany's", "2001: A Space Odyssey" ir "It's a Wonderful Life".
# import re
#
# txt1 = 'An American in Paris'
# txt2 = 'Breakfast at Tiffany\'s'
# txt3 = '2001: A Space Odyssey'
# txt4 = 'It\'s a Wonderful Life'
#
# # result = txt.translate({ord('a','A'): None})
# result1: str = re.sub('[a,e,i,o,u,A,E,I,O,U]', '', txt1)
# result2: str = re.sub('[a,e,i,o,u,A,E,I,O,U]', '', txt2)
# result3: str = re.sub('[a,e,i,o,u,A,E,I,O,U]', '', txt3)
# result4: str = re.sub('[a,e,i,o,u,A,E,I,O,U]', '', txt4)
#
# print(result1)
# print(result2)
# print(result3)
# print(result4)

########################################################################################################################
# 7. Stringe, kurį generuoja toks kodas: starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
# Surasti ir atspausdinti epizodo numerį.
# import random
# import re
# starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
# print(starWars)
#
# # res1 = int(''.join(filter(str.isdigit, starWars)))
# #print(res1)
#
# res2 = re.search('Episode (\d+)', starWars, re.IGNORECASE)
# res2.group(1)

########################################################################################################################
# 8. Suskaičiuoti kiek stringe “Don't Be a Menace to South Central While Drinking Your Juice in the Hood” yra žodžių
# trumpesnių arba lygių nei 5 raidės. Pakartokite kodą su stringu “Tik nereikia gąsdinti Pietų Centro, geriant sultis pas save kvartale”.
# txt = 'Don\'t Be a Menace to South Central While Drinking Your Juice in the Hood'
# #txt = 'Tik nereikia gąsdinti Pietų Centro, geriant sultis pas save kvartale'
# wordcount = 0
#
# words = txt.split()
#
# for word in words:
#     if len(word) <= 5:
#         wordcount += 1
#
# print (f'cia yra {wordcount} žodžių trumpesnių arba turin2iu 5 raidės')

########################################################################################################################
# 9. Parašyti kodą, kuris generuotų atsitiktinį stringą iš lotyniškų mažųjų raidžių. Stringo ilgis 3 simboliai.
# import string
# import random
#
# randomLowerLetter1 = random.choice(string.ascii_letters.lower())
# randomLowerLetter2 = chr(random.randint(ord('a'), ord('z')))
# randomLowerLetter3 = chr(random.randint(ord('a'), ord('z')))
# res = randomLowerLetter1 + randomLowerLetter2 + randomLowerLetter3
# print(f'{res}')
# txt=''
# while len(txt)!=3:
#     txt = txt + chr(random.randint(ord('a'), ord('z')))
#
# print(f'su ciklu: {txt}')

########################################################################################################################
# 10. Parašykite kodą, kuris generuotų atsitiktinį stringą su 10 atsitiktine tvarka išdėliotų žodžių, o žodžius
# generavimui imtų iš 8-me uždavinyje pateiktų dviejų stringų. Žodžiai neturi kartotis. (reikės masyvo)
import random
txt1 = 'Don\'t Be a Menace to South Central While Drinking Your Juice in the Hood'
txt2 = 'Tik nereikia gąsdinti Pietų Centro, geriant sultis pas save kvartale'
word_list = txt1.split()+txt2.split()
#print(word_list)
#print(len(word_list))
txt3=''
n = random.sample(range(len(word_list)), 10)
for i in n:
    # print(word_list[i])
    txt3 +=  word_list[i] + ' '
print(txt3)
