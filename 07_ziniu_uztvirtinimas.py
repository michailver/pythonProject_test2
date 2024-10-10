# Užduoties tikslas
#
# Suskaičiuoti kiek duonos kepalų kepykla sugebės iškepti per dieną, ar
# spės įgyvendinti visus dienos užsakymus ir suskaičiuoti kiek iš jų uždirbs
# pelno.
#
# Duomenys
# Apibrėžti duomenys:
# 1. Darbo valandų per dieną - 8 val.
from unicodedata import decimal

# Jūsų suvedami duomenys:
# 1. Kiek darbuotojas gali iškepti kepalų per valandą.
kepa_per_valanda = int(input('1. Kiek darbuotojas gali iškepti kepalų per valandą: '))
# 2. Kiek darbuotojų turi kepykla.
darbotuju_sk = int(input('2. Kiek darbuotojų turi kepykla.: '))
# 3. Vieno kepalo savikaina.
savikaina = float(input('3. Vieno kepalo savikaina: '))
# 4. Vieno kepalo pardavimo kaina.
pardavimo_kaina = float(input('4. Vieno kepalo pardavimo kaina: '))
# 5. Kiek kepykla turi tą dieną iškepti kepalų (užsakymai).
uzsakymas = int(input('5. Kiek kepykla turi tą dieną iškepti kepalų (užsakymai): '))

# Skaičiavimai
print('----------------1----------------')
# 1. Suskaičiuoti kiek kepykla per vieną darbo dieną spės iškepti duonos kepalų.

max_kiekis_diena = (darbotuju_sk * kepa_per_valanda) * 8 #8 darbo valandos
print(f'Kepykla per vieną darbo dieną spės iškepti duonos kepalų: {max_kiekis_diena}')

print('----------------2----------------')
# 2. Apskaičiuoti visų kepalų savikainą, gautas pajamas pardavus ir iš to gauto pelno dalį.
savikaina_diena = uzsakymas * savikaina
pajamos_diena = uzsakymas * pardavimo_kaina
pelnas_diena = pajamos_diena - savikaina_diena
print(f'visų kepalų savikainą: {savikaina_diena}')
print(f'gautas pajamas pardavus: {pajamos_diena}')
print(f'gauto pelno dalis: {pelnas_diena}')

print('----------------3----------------')
# 3. Patikrinti ar kepykla spės iškepti visus tos dienos užsakymus. Jei ne, suskaičiuoti kiek kepalų nespės iškepti.
if max_kiekis_diena < uzsakymas :
    kiekis_nespesim = uzsakymas - max_kiekis_diena
    print(f'AAAA! mes nespesim ishkepti: {kiekis_nespesim} kepiniu')
    print('----------------4----------------')
    print('Tures mazesni pajamas ir pelna')
    savikaina_diena = max_kiekis_diena * savikaina
    pajamos_diena = max_kiekis_diena * pardavimo_kaina
    pelnas_diena = pajamos_diena - savikaina_diena
    print(f'gautas pajamas pardavus: {pajamos_diena}')
    print(f'gauto pelno dalis: {pelnas_diena}')

