import random


def cust_range(word):
    l_word = list(word)
    for i in range(0, len(word)):
        yield l_word.pop(random.randint(0, len(l_word) - 1))


for i in cust_range('bonjour'):
    print(i)

nom_shuffle = ''.join([i for i in cust_range('Au revoir')])
print(nom_shuffle)
