import numpy as np
import pandas as pd

path = "C:\\Users\\Kasper\\Desktop"
filetype = '.xlsx'
files = ['test' + filetype, 'test1' + filetype]
dest_file = 'test2' + filetype

seperator = '------------------------------------------------------------'

print()
print('***** CONCATONATE EXCEL FILES *****')
print()

print(seperator)

try:
    df_list = [pd.read_excel(path + '\\' + i) for i in files]
except:
    print("Error in reading files from path: " + path + ',')
    print("make sure that the files are present in the given directory.")
else:
    print('Succesfully read the files:')
    for i in files:
        print(i)

print(seperator)

try:
    df2 = pd.concat(df_list).astype('float64')
except:
    print('Error occured when concatenating the dataframes.')
else:
    print('Succesfully concatenated the files.')

print(seperator)

try:
    df2.to_excel(path + dest_file, engine='xlsxwriter')
except:
    print('Error when writing to path: ' + dest_file)
else:
    print('Succesfully wrote the concatenated files to ' + dest_file + '.')

print(seperator)