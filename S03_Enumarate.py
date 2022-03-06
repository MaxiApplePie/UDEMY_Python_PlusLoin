from lorem.text import TextLorem

lorem = TextLorem(wsep=' ', srange=(8,10))

s = lorem.sentence()
print(s)

phrase = "Tempora numquam dolore dolorem quaerat modi ipsum porro numquam consectetur"

camel = ''
for i, mot in enumerate(phrase.split(), 1):
    if i == 1:
        mot = mot.lower()
    else:
        mot = mot.capitalize()
    camel += mot
print(camel)