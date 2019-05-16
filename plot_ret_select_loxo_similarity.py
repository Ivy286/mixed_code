import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

path = './tmp'
csvs = os.listdir(path)

for i, j in enumerate(csvs):
    name = os.path.splitext(j)[0]
    print(name)
    df = pd.read_csv(os.path.join(path, j))
    df.sort_values(by='similarity', ascending=False, inplace=True)
#     print(df.head())
    simi = df['similarity']
    ids = df['ID']
    index = np.arange(len(ids))
    plt.figure(figsize=(20,6))
    plt.subplots_adjust(left=0.05, bottom=0.25, right=0.98, top=0.93, hspace=0.2, wspace=0.3)
    plt.bar(index, simi, alpha=0.9, width=0.4, label='similarity', lw=1)
    plt.title(name, fontproperties='Times New Roman', fontsize=20)
    plt.grid(ls='--')
    plt.xticks(index, ids, rotation=90, fontproperties='Times New Roman', fontsize=14)
    plt.yticks(fontproperties='Times New Roman', fontsize=14)
    plt.ylabel('Similarity', fontproperties='Times New Roman', fontsize=16)
    plt.ylim(0, 1.0)
    plt.savefig('./' + str(name) + '.png', dpi=100)
    plt.clf()
