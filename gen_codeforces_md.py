# generate markdown file for list .cpp in CodeForce directory

import os
import re
from tqdm import tqdm

def get_file_name(path):
    file_list = os.listdir(path)
    file_list.sort()
    return file_list

file_list = get_file_name('./CodeForces')
# print to CodeForces.md

accepted_list = []
ongoing_list = []
for file in tqdm(file_list, desc='Finding file to print in CodeForces.md', total=len(file_list), unit='file', ncols = 100):
    # read first line of file
    with open('./CodeForces/' + file, 'r',encoding='utf8') as f:
        # pass if not .cpp
        if not re.search('\.cpp$', file):
            continue
        first_line = f.readline()
        first_line = str(first_line)
        # accepted : first line must end with 'Accepted'
        # and not case sensitive
        if re.search('Accepted$', first_line, re.IGNORECASE):
            accepted_list.append(file)
        else:
            ongoing_list.append(file)

with open('./CodeForces/CodeForces.md', 'w') as f:
    print('# CodeForces problem list', file=f)
    # table of content
    print('## Table of content', file=f)
    print('- [Accepted](#accepted)', file=f)
    print('- [Ongoing](#ongoing)', file=f)

    print('## Accepted', file=f)
    if len(accepted_list) == 0:
        print('***No accepted problem***', file=f)

    for file in tqdm(accepted_list, desc='Accepted problem', total=len(accepted_list), unit='file', ncols = 100):
        print(f'**{file[:-4]}**\n - code : [{file}](./CodeForces/{file})\n - link : [codeforces](https://codeforces.com/problemset/problem/{file[:-5]}/{file[-5]})\n', file=f)
    
    print('## Ongoing', file=f)
    if len(ongoing_list) == 0:
        print('***No on-going problem***', file=f)
    
    for file in tqdm(ongoing_list, desc='On-going problem', total=len(ongoing_list), unit='file', ncols = 100):
        print(f'**{file[:-4]}**\n - code : [{file}](./CodeForces/{file})\n - link : [codeforces](https://codeforces.com/problemset/problem/{file[:-5]}/{file[-5]})\n', file=f)