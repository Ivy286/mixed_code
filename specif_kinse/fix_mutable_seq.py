import os
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import MutableSeq
from Bio.Alphabet.IUPAC import IUPACProtein
import pandas as pd


def modified_fasta(path, file_name, muta_number, first_alphbet, last_alphbet):
    path_new = path + 'seqs/second_seq/' + file_name + '.fasta'
    # print(path_new)
    seq = [seq_record.seq for seq_record in SeqIO.parse(path_new, 'fasta')]
    seq_ = MutableSeq(str(seq[0]), IUPACProtein)
    # print(len(seq_))
    # print(seq_[int(muta_number)])
    if seq_[int(muta_number)] == first_alphbet:
        seq_[int(muta_number)] = last_alphbet
        mutable_seq = seq_.toseq()
        # rec1 = SeqRecord(mutable_seq)
        # SeqIO.write(rec1, path + file_name + '.fasta', 'fasta')
        return mutable_seq
    else:
        print(path_new, file_name, seq_[int(muta_number)], first_alphbet)
        return file_name


def fix_mutation_site(name_list, muta_list):
    for name, muta_site in zip(name_list, muta_list):
        start = muta_site[0]
        end = muta_site[-1]
        name_ = []
        seq = []
        if 1 < len(muta_site) <= 5:
            muta_num = int(muta_site[1: 4]) - 1
            mu_seq = str(modified_fasta(path, name, muta_num, start, end))
            name_.append(name)
            seq.append(mu_seq)
            df_5 = pd.DataFrame({'name': name_, 'muta_seq': seq})
            df_5.to_csv(path + 'test/5_len.csv', index=False)
            # list_new = zip(name_, seq)
            # with open(path + 'test/5_len.txt', 'w') as f1:
            #     f1.write(list_new)

        if len(muta_site) == 6:
            muta_num = int(muta_site[1: 5]) - 1
            mu_seq = str(modified_fasta(path, name, muta_num, start, end))
            name_.append(name)
            seq.append(mu_seq)
            df_6 = pd.DataFrame({'name': name_, 'muta_seq': seq})
            df_6.to_csv(path + 'test/6_len.csv', index=False)
            # list_new = zip(name_, seq)
            # with open(path + 'test/6_len.txt', 'w') as f1:
            #     f1.write('\n'.join(list_new))

        else:
            print('*' * 100)
            print(name, muta_site)


if __name__ == "__main__":
    path = './bj_ret/renova_hydra/'
    fasta_list = os.listdir(path + 'seqs/second_seq/')
    csv_path = path + 'test.csv'
    print(os.path.exists(csv_path))

    df = pd.read_csv(csv_path)
    muta_list = list(df['Mutation'])
    names = list(df['Kinase(Mutation)'])
    protein = list(df['Protein Accession #'])
    name_list = [name.replace("/", "_") + '_' + pro_id for name, pro_id in zip(names, protein)]
    fix_mutation_site(name_list, muta_list)

            # seq = [seq_record.seq for seq_record in SeqIO.parse(name, 'fasta')]
            # seq_ = MutableSeq(str(seq[0), IUPACProtein)
            # if seq_[254] = 'K'
            # mutable_seq = seq_.toseq()
            # rec1 = SeqRecord(mutable_seq)
            # SeqIO.write(rec1, 'test.fasta', 'fasta')
