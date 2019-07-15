import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np


file_path = './all.xlsx'
print os.path.exists(file_path)
df = pd.read_excel(file_path, sep=' ', column_name=['cell_permeability', 'kmeans_labels'])
# print df
# print type(df)
x1 = np.linspace(20, 39, 20)
x2 = np.linspace(63, 73, 11)
print x1, x2
y1 = df.ix[20:39, 'cell_permeability']
y2 = df.ix[20:39, 'kmeans_labels']
y3 = df.ix[63:73, 'cell_permeability']
y4 = df.ix[63:73, 'kmeans_labels']
print y1, y2, y3, y4

plt.figure(figsize=(8, 6))
plt.subplot(221)
plt.scatter(x1, y1, label="FDA", color='green')
plt.xlim(18, 42)
plt.ylim(3.2, 8.2)
plt.title("cell_permeability")
plt.legend()

plt.subplot(222)
plt.scatter(x1, y2, label="FDA", color='red')
plt.xlim(18, 42)
plt.ylim(-0.3, 1.7)
plt.title("kmeans_labels")
plt.legend()

plt.subplot(223)
plt.scatter(x2, y3, label="Terminated", color='green')
plt.xlim(61, 75)
plt.ylim(3.2, 8.2)
plt.legend()

plt.subplot(224)
plt.scatter(x2, y4, label="Terminated", color='red')
plt.xlim(61, 75)
plt.ylim(-0.3, 1.7)
plt.legend()

plt.show()
