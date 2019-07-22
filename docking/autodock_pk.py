import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import f1_score, confusion_matrix, roc_auc_score, roc_curve, auc

def autodock_evaluation(path):
    "params: path为数据地址，先要求必须为excel
     return: 在脚本所在目录下生成pk.jpg的图片和df_pk.csv的文件（供提交到atompai上使用）
    "

    df = pd.read_excel(path, header=None)
    df.columns = ['A', 'B']
    df['A'] = df['A'].values * (-1)
    fpr, tpr, thresholds = roc_curve(df['B'], df['A'])
    
    best = 0
    acc = []
    for i in thresholds:
        y_pred = np.where(df['A'] >i, 1,0)
        summ = df[df['A']>i].shape[0]
        one  = confusion_matrix(df['B'], y_pred)[1][1]
        acc.append(one/float(summ))
        
    acc = np.array(acc)
    df_pk = pd.DataFrame({'precision': acc, 'thresholds': thresholds})
    df_pk.fillna(0)
    df_pk.to_csv('df_pk.csv')
    
    plt.figure(figsize=(16, 9))
    plt.plot(thresholds, acc)
    plt.xlabel('affinity', fontsize=20)
    plt.ylabel('precision', fontsize=20)
    plt.savefig('pk.jpg')


file_path = './xxx.xlsx'
autodock_evaluation(file_path)

