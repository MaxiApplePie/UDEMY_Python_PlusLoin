

# 61 Format
print('\n** 61 ' + '**' * 20)

texte = '{} {}'.format('Laurent', 'Mollard-chaumette')
print(texte)

texte = '{1} {0}'.format('Laurent', 'Mollard-chaumette')
print(texte)

texte = '{0} {0}'.format('Laurent', 'Mollard-chaumette')
print(texte)

texte = '{0} {1}'.format('Laurent', 51)
print(texte)

texte = '{prenom} {age}'.format(prenom='Laurent', age=51)
print(texte)

texte = '{:10} {}'.format('Laurent', 'Mollard-chaumette')
print(texte)

texte = '{:>10} {}'.format('Laurent', 'Mollard-chaumette')
print(texte)

texte = '{:*>10} {:>20}'.format('Laurent', 'Mollard-chaumette')
print(texte)

texte = '{:+^15} {:>20}'.format('Laurent', 'Mollard-chaumette')
print(texte)

texte = '{:=>10} {:>20}'.format('Laurent', 'Mollard-chaumette')
print(texte)

texte = '{:.3} {}'.format('Laurent', 'Mollard-chaumette')
print(texte)

texte = '{:.3} {}'.format(2.65988, 'Mollard-chaumette')
print(texte)

# Dictionnaire
user = {'prenom': 'Pierre', 'nom': 'Durand'}
texte = '{d[prenom]} {d[nom]}'.format(d=user)
print(texte)










