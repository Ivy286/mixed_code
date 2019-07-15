import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np


file_path = './all.xlsx'
print os.path.exists(file_path)
df = pd.read_excel(file_path, sep=' ', column_name=['cell_permeability', 'solubility'])
# print df
# print type(df)
# x1 = np.linspace(0, 19, 20)
# x2 = np.linspace(63, 73, 11)
# print x1
y1 = df.ix[20:39, 'cell_permeability']
y2 = df.ix[20:39, 'solubility']
y3 = df.ix[40:57, 'cell_permeability']
y4 = df.ix[40:57, 'solubility']
y5 = df.ix[58:62, 'cell_permeability']
y6 = df.ix[58:62, 'solubility']
y7 = df.ix[63:73, 'cell_permeability']
y8 = df.ix[63:73, 'solubility']

print y1, y2, y3, y4

plt.figure(figsize=(8, 4))
plt.scatter(y1, y2, label="FDA", color='blue', linewidth=2, marker='<')
plt.scatter(y3, y4,  label="Cli", color='b', linewidth=2, marker='^')
plt.scatter(y5, y6, label="NOPR", color='r', linewidth=2, marker='s')
plt.scatter(y7, y8,  label="TEM", color='r', linewidth=2, marker='>')
plt.ylim(-10.1, -2.7)
plt.xlim(4.8, 5.8)
plt.xlabel('cell permeability')
plt.ylabel('solubility')

plt.legend(loc='lower right')
plt.show()


# plt.subplot(121)
# plt.scatter(x1, y1, label="FDA", color='green', linewidth=2)
# plt.xlim(18, 40)
# plt.ylim(-15, -1, 3)
# plt.xlabel("number")
# plt.ylabel("affinity energy")
# plt.title("affinity energy")
# plt.legend()
#
# plt.subplot(122)
# plt.scatter(x2, y2, label="Terminated", color='red', linewidth=2)
# plt.xlim(62, 74)
# plt.ylim(-15, -1)
# plt.title("affinity energy")
# plt.legend()
#
# plt.show()
