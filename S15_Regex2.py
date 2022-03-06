import re

# print(re.match(r'\+', 'Pierre Dupont + Laurent Mollard-Chaumette'))
# print(re.search(r'\+', 'Pierre Dupont + Laurent Mollard-Chaumette'))

texte = 'item01 | item02 - item03 - item04 | item05'
print(re.split(r' \| | - ', texte))

# Vérifier quels numéros dans la liste de numéros de téléphones sont valides.
p# Un numéro valide en France doit être composée d'une suite de 5 nombres avec 2 chiffres. La première série de
# nombres doit être comprise entre 01 et 07.
# Cela donne donc 0A-XX-XX-XX-XX où A est un nombre compris entre 1 et 7 et X un nombre compris entre 0 et 9.

numeros_de_telephone = ['06-71-45-34-23',
                        '02-12-33-75-12',
                        '00-23-14-52-44',
                        '514-235-0293',
                        '03-52-31-56-34']

for i in numeros_de_telephone:
    print(re.match('0[1-7]{1}(-\d\d){4}', i))

# Le numéro 06-71-45-34-23 est valide
# Le numéro 02-12-33-75-12 est valide
# Le numéro 00-23-14-52-44 est invalide
# Le numéro 514-235-0293 est invalide
# Le numéro 03-52-31-56-34 est valide


adresses_mail = ['christian_martin@gmail.com',
                 'JaiOublieLarobasegmail.com',
                 'MarieHutchinson03523@yahoo.co.uk',
                 'UnEaDreSSeMail!38BIZarre@unSiTeBizarre.com',
                 'ceciNestPasUneDresseMail']

print('\n' + '*' * 25 + '\n')
for adresse_mail in adresses_mail:
    print(re.search(r'.+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+', adresse_mail))
    # " adresse_valide = re.search(r'.+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+', mail)"

# L'adresse christian_martin@gmail.com est valide
# L'adresse JaiOublieLarobasegmail.com est invalide
# L'adresse MarieHutchinson03523@yahoo.co.uk est valide
# L'adresse UnEaDreSSeMail!38BIZarre@unSiTeBizarre.com est valide
# L'adresse ceciNestPasUneDresseMail est invalide
