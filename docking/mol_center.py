from base_model import cut_spec_mol2, is_not_empty

file_path = '/home/xh/2ckj_ligand.mol2'
write_path = '/home/xh/exercise.txt'
cut_spec_mol2(file_path, write_path)

with open(write_path, 'r') as f:
    text = f.readlines()
    print(text[1:])
    sum_x, sum_y, sum_z = 0.00, 0.00, 0.00
    for i in text[1:]:
        lst = list(filter(is_not_empty, i.strip().split(' ')))
        sum_x = sum_x + float(lst[2])
        sum_y += float(lst[3])
        sum_z += float(lst[4])

    x_center, y_center, z_center = sum_x/len(lst), sum_y/len(lst), sum_z/len(lst)
print(x_center, y_center, z_center)


'''

# three methods for deleting empyt str or None str in a list

lst = ['A', '', 'B', None, 'C', '  ']
#first

def is_not_empty(s):
    return s and len(s.strip()) > 0
print(list(filter(is_not_empty, lst)))

#second
temp = []
for i in lst:
    if i:
        temp.append(i)
print(temp)

#third
# filter(map(s and len(s.strip()) > 0, lst))

'''
