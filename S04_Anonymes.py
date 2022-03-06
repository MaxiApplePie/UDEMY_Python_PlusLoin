import os

fichiers = [r'D:\DEV\UDEMY_Tuto_45h_PYTHON\UDEMY_FullPython\John.py',
            r'D:\DEV\UDEMY_Tuto_45h_PYTHON\UDEMY_FullPython\pabob.txt',
            r'D:\DEV\UDEMY_Tuto_45h_PYTHON\UDEMY_FullPython\maurice.pptx']

get_fichier = lambda f: os.path.split(f)[-1]
get_ext = lambda f: os.path.splitext(f)[-1]
del_point = lambda f: f.replace('.', '')
process = lambda f: del_point(get_ext(get_fichier(i)))

for i in fichiers:
    print(process(i))

print('\n*' * 2)
multiplication = lambda a, b: a * b
print(multiplication(2, 6))





