def concatenation_chemin(*args):
    elemnts = list(args)
    return '/'.join(elemnts)


chemin_complet = concatenation_chemin('C:/Users', 'OMEN', 'PycharmProjects')
print(chemin_complet)
