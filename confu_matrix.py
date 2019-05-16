from sklearn.metrics import confusion_matrix
import pandas as pd
import os
import numpy as np

file_path = '/home/xh/Desktop/output_predict.xls'
print os.path.exists(file_path)
df = pd.read_excel(file_path, sep=' ', column_name=['labels', 'assay'])
# print df
# print type(df)
a = df.ix[:, 'labels']
b = df.ix[:, 'assay']
print a, b
print confusion_matrix(a, b)

# if __name__ == "__main__":
#     a = [[13, 0, 0],
#          [0, 10, 6],
#          [0, 0, 9]]
#     b = [[1, 0, 0],
#          [0, 0.62, 0.38],
#          [0, 0, 1]]
#
#     print(confusion_matrix(a, b))
