def addition(*args):
    print(type(args))
    return sum(args)

def liste_invites(invite_vip, *args, **kwargs):
    print('{vip} est un invité VIP !'.format(vip=invite_vip))
    for i in args:
        print('{normal} est un invité sandard !'.format(normal=i))
    indesirables = kwargs.get('indesirables')
    print(type(indesirables))
    print(indesirables)
    if indesirables:
        print('Par contre, ceux-la restent dehors : {inde}'.format(inde=','.join(indesirables)))

print(addition(3, 2))

liste_invites('Bib', 'Bob', 'Bab', 'Bub', indesirables=['ob', 'ab', 'ub'])