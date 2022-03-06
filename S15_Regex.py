import re

print(re.match(r'[a-z]+\d{2}', 'item01'))
# ok
print(re.match(r'.[a-zA-Z]+\s\w+', ' Pierre Dupont'))
# ok
print(re.match(r'\s+', 'pierre  dupont'))
# None
print(re.match(r'\w+', 'pierre dupont'))
# ok
print(re.match(r'\w+([-+=]?)', 'pierre-dupont'))
# ok
print(re.match(r'\w+([-+=]?)', 'pierre/dupont'))
# ok
print(re.match(r'\w+([-+=]+)', 'pierre/dupont'))
# None