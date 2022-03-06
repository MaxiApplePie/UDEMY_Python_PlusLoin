import os

cur_dir = os.path.dirname(__file__)

dossier_rendu_01 = os.path.join(cur_dir, 'rendus_01')
dossier_rendu_02 = os.path.join(cur_dir, 'rendus_02')

fichiers_01 = os.listdir(dossier_rendu_01)
fichiers_02 = os.listdir(dossier_rendu_02)

fichiers_00 = list()
for i in range (1, 101):
    fichiers_00.append(f'{str(i).zfill(4)}.jpg')

# print(set(fichiers_00).difference(set(fichiers_01)))
# print(set(fichiers_00).difference(set(fichiers_02)))
# print(sorted(list((set(fichiers_00).difference(set(fichiers_01))).intersection(set(fichiers_00).difference(set(
#     fichiers_02))))))

fichiers_rendus = set(fichiers_01) | set(fichiers_02)
toutes_les_images = set([str(i).zfill(4) + '.jpg' for i in range(1, 101)])

images_manquantes = toutes_les_images - fichiers_rendus
print(sorted(list(images_manquantes)))

all_images = set(["{:0>4d}.jpg".format(i+1) for i in range(100)])

# Le but de l'exercice est de trouver quels images sont manquantes à la fois dans le dossier 1 et le dossier 2.
all_images_present = set(fichiers_01) | set(fichiers_02)

missing_images = list(all_images - all_images_present)
missing_images.sort()
print(missing_images)