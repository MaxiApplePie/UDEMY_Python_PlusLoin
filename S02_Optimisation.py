import random
import time

a = time.time()
with open("nombres_aleatoires.txt", 'w') as f:
    to_write = ''
    for _ in range(50000000):
        to_write += str(random.randint(0, 10))
    f.write(to_write)
b = time.time()
print(f"{b - a}")
# 6.158463954925537

a = time.time()
with open("nombres_aleatoires.txt", 'w') as f:
    to_write = []
    for _ in range(50000000):
        to_write.append(str(random.randint(0, 10)))
    f.write(''.join(to_write))
b = time.time()
print(f"{b - a}")

# 130.42420601844788
# 52.16983771324158

