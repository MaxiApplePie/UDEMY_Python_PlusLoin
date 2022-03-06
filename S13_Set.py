mon_set = {1, 2, 3, 4, 'a', 'a', 'a'}
print(mon_set)
mon_set.add(666)
print(mon_set)

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7, 8, 9}
print(set_b.union(set_a))
print(set_a.intersection(set_b))
print(set_a | set_b)
print(set_a - set_b)