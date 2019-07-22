import os
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import MutableSeq
from Bio.Alphabet.IUPAC import IUPACProtein
import pandas as pd
import requests

seq = [seq_record.seq for seq_record in SeqIO.parse('example.fasta', 'fasta')]
seq_ = MutableSeq(str(seq), IUPACProtein)
seq_[254] = 'K'
mutable_seq = seq_.toseq()
rec1 = SeqRecord(mutable_seq)
SeqIO.write(rec1, 'test.fasta', 'fasta')

# mutable_seq = Bio.Seq.MutableSeq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA", IUPAC.unambiguous_dna)
# mutable_seq[5] = 'C'
# print(mutable_seq[5])
#
# new_seq = mutable_seq.toseq()
# print(new_seq)

path = './bj_ret/renova_hydra/seqs/second_seq/'
# df = pd.read_excel(path + 'NIHMS751504-supplement-3_use.xlsx', usecols=[0, 3])
df = pd.read_excel(path + 'NIHMS751504-supplement-3_us4e.xlsx')

seq_id = list(df['Protein Accession #'])
names = list(df['Kinase(Mutation)'])

name_list = [name.replace("/", "_") for name in names]
print(name_list)
seq_list = []
for one, two in zip(name_list, seq_id):
    load_path = 'https://www.uniprot.org/uniprot/' + two + '.fasta'
    t = requests.get(load_path)
    new_t = t.text.split('\n', 1)[1]
    seq = new_t.replace('\n', '')
    print(len(seq))
    seq_list.append(seq)
print(len(seq_list))
# df_new = df.iloc[:2].copy()   # this is necessary when using part of data for test
df['Sequence'] = seq_list
print(df)
df.to_csv(path + 'add_seqs.csv', index=False)
#     write_path = path + str(one) + '_' + str(two) + '.fasta'
#     with open(write_path, 'w') as f1:
#         f1.write(t.text)
# print("finished !")
