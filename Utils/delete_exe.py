# delete all .exe files in the specified directory

import os
import re
import datetime

f = open('../log.log', 'a')

def delete_exe(path):
    file_list = os.listdir(path)
    # get only .exe file
    file_list = [file for file in file_list if re.search('\.exe$', file)]
    for file in file_list:
        os.remove(path + '/' + file)
        # show progress
        print('Delete ' + file + ' in ' + path)
        f.write('Delete ' + file + ' in ' + path)

if __name__ == '__main__':
    # append to log file with time
    print('delete_exe.py : ' + str(datetime.datetime.now()), file=f)
    paths = ['C:/Users/jiray/Desktop/Algorithm Design/CodeForces',
             'C:/Users/jiray/Desktop/Algorithm Design/grader']
    for path in paths:
        try:
            delete_exe(path)
        except:
            print('No .exe file in ' + path)
            f.write('No .exe file in ' + path)

f.write('\n\n')
f.close()