import json


from os import RTLD_DEEPBIND


f = open('modes.json')
data = json.load(f)

# for key_1 in data.keys():
#     print(key_1)
#     for key_2 in data[key_1]:
#         print(key_2)
#         for key, val in key_2.items():
#             print(key)
#             print(val)

for atom in data['atom']:
    print(atom)
    for key, val in atom.items():
        print(key, val)

for phonon in data['phonon']:
    for mode in phonon['mode']:
        print(mode['eigenvalue'])
        print(*mode['eigenvector'])
    


f.close()