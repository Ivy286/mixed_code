import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np


file_path1 = './homo/egfr/models/dope/dope.xlsx'
# file_path2 = '/home/xh/0.xlsx'
print os.path.exists(file_path1)
df1 = pd.read_excel(file_path1, sep=' ', column_name=['label', 'egfr', 'swiss', 'single',  'multi', 'loop1', 'loop2', 'multi1', 'loop3', 'loop4', 'multi2', '4lqm'])
# df2 = pd.read_excel(file_path1, sep=' ', column_name=['# RES', 'TAL'])
# print df
# print type(df)
# x1 = np.linspace(20, 39, 20)
# x2 = np.linspace(63, 73, 11)
# print x1, x2
x1 = df1.ix[:, 'label']
y1 = df1.ix[:, 'egfr']
y2 = df1.ix[:, 'single']
y3 = df1.ix[:, 'multi']
y4 = df1.ix[:, 'loop1']
y5 = df1.ix[:, 'loop2']
y6 = df1.ix[:, 'swiss']
y7 = df1.ix[:, 'loop3']
y8 = df1.ix[:, 'multi1']
y9 = df1.ix[:, 'loop4']
y10 = df1.ix[:, 'multi2']
y11 = df1.ix[:, '4lqm']
print x1, y2

plt.figure(figsize=(8, 6))
# plt.subplot(221)
plt.plot(x1, y1, label="experiment", color='r', linewidth=2, ls='--')
plt.plot(x1, y6, label="swiss-model", color='grey', linewidth=2)
# plt.plot(x1, y2, label="single-model", color='y', linewidth=2)
# plt.plot(x1, y3, label="multi-model", color='g', linewidth=2)
# plt.plot(x1, y4, label="loop1-model", color='blue', linewidth=2)
# plt.plot(x1, y5, label="loop2-model", color='fuchsia', linewidth=2)
# plt.plot(x1, y7, label="loop3-model", color='darkblue', linewidth=2)
# plt.plot(x1, y8, label="multi1-model", color='pink', linewidth=2)
# plt.plot(x1, y9, label="loop4-model", color='pink', linewidth=2)
# plt.plot(x1, y10, label="multi2-model", color='darkorange', linewidth=2)
plt.plot(x1, y11, label="single-4lqm", color='green', linewidth=2)

plt.plot(x1, [-0.03]*len(x1), color='black', linewidth=1.5, ls='--')
plt.xlim(-10, 350)
plt.ylim(-0.07, 0.0)
plt.title("DOPE Score")
plt.legend()
plt.show()
