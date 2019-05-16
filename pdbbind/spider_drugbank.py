import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
file_path = '/home/dongha/Desktop/PP_score_topk3com202node2vec100.csv'
with open(file_path, 'r') as f:
    text = f.readlines()
    for i in text[61:73]:
        i_ = i.split(',')
        id = i_[3].split()[0]
        read_path = 'https://www.drugbank.ca/structures/small_molecule_drugs/' + id + '.sdf?type=3d'
        t = requests.get(read_path)
        write_path = '/home/dongha/Desktop/drugs/' + id + '.sdf'
        with open(write_path, 'w') as f1:
            f1.write(t.text)
