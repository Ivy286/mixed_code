
def is_not_empty(s):
    return s and len(s.strip()) > 0


def cut_spec_mol2(mol2_path, write_path):
    with open(mol2_path, 'r') as f:
        text = f.readlines()

        flag = False
        cont = []

        for line in text:
            # print(line)

            if line.startswith('@<TRIPOS>ATOM'):
                flag = True

            if line.endswith('@<TRIPOS>BOND\n'):
                flag = False
                break

            if flag:
                cont.append(line)

            with open(write_path, 'w') as f1:
                f1.writelines(cont)
    return None
