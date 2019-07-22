import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np


file_path1 = './dope1.xlsx'
file_path2 = './0.xlsx'
print os.path.exists(file_path1)
df1 = pd.read_excel(file_path1, sep=' ', column_name=['label', 'web', 'single',  'mult', 'loop'])
# df2 = pd.read_excel(file_path1, sep=' ', column_name=['# RES', 'TAL'])
# print df
# print type(df)
# x1 = np.linspace(20, 39, 20)
# x2 = np.linspace(63, 73, 11)
# print x1, x2
x1 = df1.ix[:, 'label']
y1 = df1.ix[:, 'web']
y2 = df1.ix[:, 'single']
y3 = df1.ix[:, 'mult']
y4 = df1.ix[:, 'loop']
# y3 = df.ix[63:73, '# RES']
# y4 = df.ix[63:73, 'TAL']
print x1, y1

plt.figure(figsize=(8, 6))
# plt.subplot(221)
plt.plot(x1, y1, label="web-model", color='r', linewidth=1.5)
plt.plot(x1, y2, label="single-model", color='y', linewidth=1.5)
plt.plot(x1, y3, label="mult-model", color='g', linewidth=1.5)
plt.plot(x1, y3, label="loop-model", color='b', linewidth=1.5)
plt.plot(x1, [-0.03]*len(x1), color='black', linewidth=1.5, ls='--')
plt.xlim(-10, 700)
plt.ylim(-0.08, 0.02)
plt.title("DOPE Score")
plt.legend()

# plt.subplot(222)
# plt.scatter(x1, y2, label="FDA", color='red')
# plt.xlim(18, 42)
# plt.ylim(-0.3, 1.7)
# plt.title("kmeans_labels")
# plt.legend()
#
# plt.subplot(223)
# plt.scatter(x2, y3, label="Terminated", color='green')
# plt.xlim(61, 75)
# plt.ylim(3.2, 8.2)
# plt.legend()
#
# plt.subplot(224)
# plt.scatter(x2, y4, label="Terminated", color='red')
# plt.xlim(61, 75)
# plt.ylim(-0.3, 1.7)
# plt.legend()
#
plt.show()
