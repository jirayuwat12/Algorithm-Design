# delete all .exe files in the specified directory

import os
import re

def delete_exe(path):
    file_list = os.listdir(path)
    # get only .exe file
    file_list = [file for file in file_list if re.search('\.exe$', file)]
    for file in file_list:
        os.remove(path + '/' + file)

if __name__ == '__main__':
    paths = ['C:/Users/jiray/Desktop/Algorithm Design/CodeForces',
             'C:/Users/jiray/Desktop/Algorithm Design/grader']
    for path in paths:
        try:
            delete_exe(path)
        except:
            print('No .exe file in ' + path)