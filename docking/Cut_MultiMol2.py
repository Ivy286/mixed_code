import pandas
import os


def cut_spec_mol2(mol2_path, write_path, startstr):
    with open(mol2_path, 'r') as f:
        text = f.readlines()
        print(text)
        flag = False
        cont = []

        for line in text:
            # print(line)

            if line.startswith(startstr):
                print('********')
                flag = True

            if flag:
                cont.append(line)

            if line.endswith('@<TRIPOS>SUBSTRUCTURE\n'):
                print('$$$$$$$$$')
                flag = False
                break
        print(cont)

        with open(write_path, 'w+') as f1:
            f1.write('abc')
            # cont.insert(0, '@<TRIPOS>MOLECULE\n' + startstr + '\n')
            f1.writelines(cont)
    return None


file_dir = '/data/docking/gout.prj/xo_2ckj/'
print(os.path.exists(file_dir))

active_path = file_dir + 'exercise.txt'
num = []
with open(active_path, 'r') as f:
    text = f.readlines()
    for line in text[1:]:
        num.append(line.split()[0])
print(num)

mol_path = file_dir + 'exercise.mol2'
count = []
for id in num:
    writ_path = file_dir + 'final_active113/' + str(id) + '.mol2'
    if id not in count:
        print('8888888888888888')
        cut_spec_mol2(mol_path, writ_path, 'chem_152')
        count.append(id)
    print(len(count))
    # continue

