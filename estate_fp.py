import numpy as np
import os
import pandas as pd

from rdkit.Chem.EState.Fingerprinter import FingerprintMol
from rdkit.Chem import MolFromSmiles
from sklearn.cluster import KMeans

def read_smiles_txt(file_path):
    file = open(file_path)
    smiles_list = []
    for line in file.readlines():
        smiles_list.append(line.strip())
    smiles_list.pop(-1)
    file.close()
    return smiles_list

def transpose(X):
    m, n = len(X), len(X[0])
    return [[X[i][j] for i in range(m)] for j in range(n)]

def write_excel(two_list, save_txt_dir):
    two_list = transpose(two_list)
    #print ('two_list:', two_list)
    print ('list length should be 3', len(two_list))
    df = pd.DataFrame(two_list, columns=['smiles', 'labels']) #columns=['origin smiles', 'generate smiles', 'valid smiles'])
    if os.path.exists(save_txt_dir):
        txt_file_path = os.path.join(save_txt_dir, 'output_predict.xlsx')
    else:
        raise AssertionError
    writer = pd.ExcelWriter(txt_file_path)
    df.to_excel(writer, 'Sheet1')
    writer.save()

if __name__=='__main__':
    txt_path = '/home/xh/Documents/egfr/egfr_all.txt'
    smiles_list = read_smiles_txt(txt_path)
    all_fp = []
    for smiles in smiles_list:
        mol = MolFromSmiles(smiles)
        all_fp.append(FingerprintMol(mol)[1])
    print ('all_fp', len(all_fp))
    x = np.array(all_fp)
    kmeans = KMeans(n_clusters=2, random_state=0).fit(x)
    labels = kmeans.labels_
    print ('labels', labels)
    two_list = [smiles_list, labels]
    save_dir = '/home/xh/Desktop/egfr/'
    write_excel(two_list, save_dir)


