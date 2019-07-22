import pubchempy as pcp
import pandas as pd
import os

path = './bj_ret/renova_hydra/'
cid_path = path + 'data_ks_profiling5.xlsx'
print(os.path.exists(cid_path))

df = pd.read_excel(cid_path)
df_new = df.drop_duplicates(['CID'])
cid_list = df_new['CID'].tolist()
print(len(cid_list))
smi_list = []
i = 0
cid_new = []
for one in cid_list:
    try:
        c = pcp.Compound.from_cid(one)
        smi_list.append(c.canonical_smiles)
        cid_new.append(one)
    except:
        print(one)
        continue
    i += 1
    print(i)
df_smi = pd.DataFrame({'cid': cid_new, 'smiles': smi_list})
df_smi.to_csv(path + 'cid_smiles.csv', index=False)
print('Finished!')
