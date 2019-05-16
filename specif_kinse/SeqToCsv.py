import os
import pandas as pd

def read_seqfile(seq_path):
    pdb_id = []
    seq = []
    for i in os.listdir(seq_path):
        a = os.path.splitext(i)
        pdb_id.append(a[0])
    return pdb_id

def read_fasta(pdb_id):
    fasta_list = []
    path = []
    for j in pdb_id:
        fast_path = seq_path + j + '.fasta'
        path.append(fast_path)
    for item in path:
        with open(item, 'r') as f:
            seq1 = []
            for jj in f.readlines()[1:]:
                seq1.append(jj.strip())
            seq_ = "".join(seq1)
            fasta_list.append(seq_)
    return fasta_list


if __name__=="__main__":
    seq_path = '/home/xh/Documents/research/bj_ret/seqs/'
    smiles = ['CC1=CC[C@H](C(C)=C)CC1']*24
    Molecule_id = ['1']*24
    pdb_id = read_seqfile(seq_path)
    seq_id = read_fasta(pdb_id)
    # print(seq_id)
    # list_all = [Molecule_id, smiles, pdb_id, seq_id]
    # name = ['Molecule_ID', 'Smiles', 'Protein_ID', 'Sequence']
    result = pd.DataFrame({'Molecule_ID': Molecule_id, 'Smiles': smiles, 'Protein_ID':pdb_id, 'Sequence': seq_id})
    # print(result)
    write_path = '/home/xh/Documents/research/bj_ret/test.csv'
    # print(path)
    result.to_csv(write_path, index=False)

