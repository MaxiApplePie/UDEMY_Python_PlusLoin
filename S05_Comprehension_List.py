ma_liste = [1, 2, 3, 4, 5]
ma_lise_double = []

# for i in ma_liste:
#     ma_lise_double.append(2 * i)

# 1
liste = [1, 2, 3, 4, 5]
liste_double = [2 * n for n in liste]
# 2
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
liste_double = [i * 2 for i in liste if i > 0]
# 3
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
liste_double = [i * 2 if i > 0 else i * 3 for i in liste]
# 4
liste_finale = [(a, b) for a in range(10) for b in range(2)]

# Avec MAP
r = map(lambda x: x * x, ma_liste)
print(list(r))


liste = [1, 2, 3, 4, 5]
liste_double = []

for i in liste:
    liste_double.append(i * 2)
