import random


class IterLetter:
    def __init__(self, mot):
        self.mot = mot
        self.compteur_de_lettres = 0
        self.mot_restant = list(mot)

    def __iter__(self):
        return self

    def __next__(self):
        self.compteur_de_lettres += 1
        if self.compteur_de_lettres <= len(self.mot):
            return self.mot_restant.pop(random.randint(0, len(self.mot_restant) - 1))
        else:
            raise StopIteration()



word = 'Bonjour'
nom_random = IterLetter(word)
nom_melange = [x for x in nom_random]
print(''.join(nom_melange).title())
for l in nom_random:
    print(l)

