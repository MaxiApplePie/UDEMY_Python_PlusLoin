import os

# 1
age = 17
print('Majeur' if age >= 18 else 'Mineur')

# 2
fichier = r'C:\Users\OMEN\PycharmProjects\AllerPlusLoin\S02_Optimisation.rpy'
extension = 'python' if os.path.splitext(fichier)[1].strip('.') == 'py' else 'invalide'
print('Le fichier {} est de type {}'.format(fichier, extension))

