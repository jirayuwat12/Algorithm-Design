# generate markdown file for list .cpp in CodeForce directory

import os
import re
from tqdm import tqdm


def get_file_name(path):
    file_list = os.listdir(path)
    # sort by custom function that sort by problem number
    # get only .cpp file
    file_list = [file for file in file_list if re.search('\.cpp$', file)]
    def custom_sort(file):
        return int(file[:-5])
    file_list.sort(key=custom_sort)
    
    return file_list
# scrap problem name from codeforces
def web_scrap(file):
    url = 'https://codeforces.com/problemset/problem/' + file[:-5] + '/' + file[-5]
    # print(url)
    import requests
    from bs4 import BeautifulSoup
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # get name
    problem_name = soup.find('div', class_='title').text
    problem_name = problem_name.replace('\n', '')
    # get difficulty
    difficulty = soup.find('div', id='sidebar').find('span', title='Difficulty').text.strip()[1:]
    return problem_name, difficulty

file_list = get_file_name('./CodeForces')
# data preparation
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
# print section
with open('./CodeForces/README.md', 'w') as f:
    print('# CodeForces problem list', file=f)

# table of content
    print('## Table of content', file=f)
    print('- [Statistic](#statistic)', file=f)
    print('- [Ongoing](#ongoing)', file=f)
    print('- [Accepted](#accepted)\n', file=f)
    print("<u>**Note**</u> : *recommend to search with problem\'s code*</u>", file=f)
# stat show in table
    print('## Statistic', file=f)
    print(f'|Name|Amount|', file=f)
    print(f'|-------------------------------------|--------------| ', file=f)
    print(f'|Number of accepted problem | {len(accepted_list)} | ', file=f)
    print(f'|Number of on-going problem | {len(ongoing_list)} | ', file=f)
    print(f'|**Total**    | {len(accepted_list) + len(ongoing_list)}| ', file=f)
# on going
    print('## Ongoing', file=f)
    if len(ongoing_list) == 0:
        print('***No on-going problem***', file=f)
    
    for file in tqdm(ongoing_list, desc='On-going problem', total=len(ongoing_list), unit='file', ncols = 100):
        name, difficulty = web_scrap(file)
        print(f'**{file[:-5]} {name} ({difficulty})**\n - code : [{file}](./CodeForces/{file})\n - link : [codeforces](https://codeforces.com/problemset/problem/{file[:-5]}/{file[-5]})\n', file=f)
# accepted
    print('## Accepted', file=f)
    if len(accepted_list) == 0:
        print('***No accepted problem***', file=f)

    for file in tqdm(accepted_list, desc='Accepted problem', total=len(accepted_list), unit='file', ncols = 100):
        name, difficulty = web_scrap(file)
        print(f'**{file[:-5]} {name} ({difficulty})**\n - code : [{file}](./CodeForces/{file})\n - link : [codeforces](https://codeforces.com/problemset/problem/{file[:-5]}/{file[-5]})\n', file=f)
    
# append to log with time stamp
import datetime
with open('log.log', 'a') as f:
    print(f'gen_codeforces_md.py : {datetime.datetime.now()}', file=f)
    print(f'Number of accepted problem : {len(accepted_list)}', file=f)
    print(f'Number of on-going problem : {len(ongoing_list)}', file=f)
    print(f'Total : {len(accepted_list) + len(ongoing_list)}', file=f)
    print('', file=f)