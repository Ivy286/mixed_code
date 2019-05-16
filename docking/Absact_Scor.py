import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
import os

'''
file_dir = '/data/docking/gout.prj/xo_2ckj/'
print(os.path.exists(file_dir))

active_path = file_dir + 'dock_active113_1.rept'
cids = []
scores = []
with open(active_path, 'r') as f:
    text = f.readlines()
    for line in text[12:130]:
        # print(line.split())
        cid_ = line.split()
        # print(len(cid_))
        cid = cid_[1]
        score = line.split()[3]
        if cid not in cids:
            cids.append(cid)
            scores.append(score)
# print(cids, scores, len(cids))
df_ = pd.DataFrame({'cids': cids, 'gscore': scores})
df_.to_csv(file_dir + 'temp.csv')
'''

ic_path = '/home/xh/Documents/research/gout/fpocket_docking.xlsx'
print(os.path.exists(ic_path))

df = pd.read_excel(ic_path, sheet_name='Sheet')
df1 = df[['no.', 'IC50(nm)']]

print(df1)
df1['no.'] = df1['no.'].astype('category')
df1['no.'].cat.set_categories(cids, inplace=True)
df1.sort_values('no.', inplace=True)
print(df1)

df2 = pd.read_excel(ic_path, sheet_name='Sheet1')
x1 = df2['no.']
y1 = df2['IC50(nm)']
y2 = df2['gscore']
y3 = df2['pic50']

print(np.corrcoef(y2, y3))
print(stats.pearsonr(y2, y3))
print(df2[['pic50', 'gscore']].corr())

plt.scatter(x1, y1)
plt.scatter(x1, y2)
plt.show()

