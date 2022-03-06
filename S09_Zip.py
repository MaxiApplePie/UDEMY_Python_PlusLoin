from pprint import pprint

l1 = [1, 2, 3, 4, 5]
l2 = ['t', 'y', 'u', 'i', 'o', 'p']
l3 = ['t', 'y', 'u', 'i', 'o', 'p']

l3 = zip(l1, l2, l3)
print(list(l3))

import string
# print(string.ascii_lowercase)
prenom = 'Astrid'
# print(prenom.index('r'))

join_liste = zip(prenom, [string.ascii_lowercase.index(c) + 1 for c in prenom.lower()])
pprint(list(join_liste))