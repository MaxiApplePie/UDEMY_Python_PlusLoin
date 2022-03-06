import os
from collections import defaultdict
# 52 __file__
from pprint import pprint

# print('\n** 52 ' + '**' * 20)
# print(os.__file__)
# print(os.path.__file__)
# print(__file__)
# print(os.path.dirname(__file__))
# print(os.path.splitext(__file__)[0])
# print(os.path.splitext(__file__)[1])
#
# # 53 Filter
# print('\n** 53 ' + '**' * 20)
# tags_photos = ['Juin', 'Bresil', 'Mars', '21', None]
# print('-'.join(filter(None, tags_photos)))
# fichiers = '-'.join(filter(None, ([i for i in tags_photos])))
# fichiers1 = '-'.join([i for i in tags_photos if i])
# print(fichiers)
# print(fichiers1)
#
# # 54 Chainage de comparateurs
# print('\n** 54 ' + '**' * 20)
# nombre = 25
# if 1 < nombre < 50:
#     print('Le nombre est compris entre 1 et 50')
#
# # 55 Boucle for else
# print('\n** 55 ' + '**' * 20)
# for tag in tags_photos:
#     if tag == 'Juin':
#         print('ok')
#         break
# else:
#     print('Problem')
#
# # 56 Inverser les valeurs d'un dictionnaire
# print('\n** 56 ' + '**' * 20)
# LONG_NAMES = {'anm_scn': 'Animation Scene',
#               'anm_out': 'Animation Publish',
#               'sim_scn': 'Simulation Scene',
#               'sim_out': 'Simulation Publish'}

# a = list(zip(LONG_NAMES.values(), LONG_NAMES.keys()))
# print(type(a))
# print(a)
# SHORT_NAMES = dict(zip(LONG_NAMES.values(), LONG_NAMES.keys()))
# print(SHORT_NAMES)
# print(SHORT_NAMES.get('Simulation Scene'))
# print(LONG_NAMES.get('sim_out'))

# 57 aplatir une liste / Doublons
print('\n** 57 ' + '**' * 20)
my_list = [[1, 2, 3], [2, 4, 8, 9], [12, 1, 4]]
my_flat_list = sum(my_list, [])    # Surprenant ((
print(my_flat_list)
my_sigleton_list = sorted(list(set(my_flat_list)))
print(my_sigleton_list)

# 58 Enlever des elements d'une liste
print('\n** 58 ' + '**' * 20)
prenom = 'Laurent'
nom = 'Mollard'
age = 51
my_profile = [prenom, nom, age]
print(my_profile)
my_profile2 = [x for x in my_profile if isinstance(x, str)]
print(my_profile2)
nom_complet = ' '.join(my_profile2)
print(nom_complet)

# 59 DefaultDict
# print('\n** 59 ' + '**' * 20)
mot = 'anticonstitutionnellement'
d = defaultdict(int)
for lettre in mot:
    d[lettre] += 1
print(d)





















