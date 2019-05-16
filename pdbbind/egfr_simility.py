import os
import shutil
from rdkit import Chem
from rdkit import DataStructs
from rdkit.Chem import MolFromMol2File, MACCSkeys
from rdkit.Chem.EState.Fingerprinter import FingerprintMol


def MACCS_keys_similarity(mol_1, mol_2):
    fps_1 = MACCSkeys.GenMACCSKeys(mol_1)
    fps_2 = MACCSkeys.GenMACCSKeys(mol_2)
    similarity = DataStructs.FingerprintSimilarity(fps_1, fps_2)
    return similarity


def ligand_file(path):
        if os.path.isfile(path):
                shutil.copy(path, '/home/xh/ligand_dir')


def mol2_mol(mol2_file):
    mol_1 = Chem.MolFromMol2File(mol2_file)
    mol_2 = Chem.MolFromMol2File('/home/xh/gefitinib.mol2')
    return MACCS_keys_similarity(mol_1, mol_2)

file_path = '/home/xh/Documents/databases/egfr_pdbid.txt'
with open(file_path, 'r') as f:
        pdb_ligand = []
        pdb_id = []
        for line in f.readlines():
                line_array = line.split(' ')
                pdb_id.append(line_array[0])
                pdb_ligand.append(line_array[0] + '_ligand.mol2')
#print pdb_ligand
list1 = []
list2 = []
for dre in pdb_id:
        new_dre = '/home/xh/Documents/databases/pdbbind_v2015/' + str(dre.strip()) + '//' + str(dre.strip() + '_ligand.mol2')
        #print new_dre
        ligand_file(new_dre)
        list1.append(str(mol2_mol(new_dre)))
with open('/home/xh/ligand_dir/gefitinib.txt', 'w') as f1:
    for i, m in zip(pdb_ligand, list1):
        f1.write(str(i + '\t' + m + '\n'))



