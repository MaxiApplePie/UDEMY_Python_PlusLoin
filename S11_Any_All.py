import os

fichiers = ['C:/Users/OMEN/PycharmProjects/fichier1.txt',
            'C:/Users/OMEN/PycharmProjects/fichier2.jpeg',
            'C:/Users/OMEN/PycharmProjects/fichier3.py',
            'C:/Users/OMEN/PycharmProjects/fichier4.bmp',
            'C:/Users/OMEN/PycharmProjects/fichier5.bmp']

au_moins_un_png = any(os.path.splitext(f)[1].strip('.') == 'png' for f in fichiers)
tous_des_jpg = all(os.path.splitext(f)[1].strip('.') == 'jpg' for f in fichiers)
print(au_moins_un_png)
for f in fichiers:
    print(os.path.splitext(f)[1].strip('.'))