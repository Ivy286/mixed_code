import glob
# import session

import os
os.chdir('/Users/xuhe/Desktop/tmp')

path_file_number = glob.glob(pathname='Adaptivaty-1*.odb')
for i in path_file_number:
    odb_name = r"C:\temp" + '\\' + str(i)
    print(odb_name)

