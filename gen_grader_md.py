import datetime
import os
import time
import json
from selenium_utils import get_problem_info
from linebot import LineBotApi
from linebot.models import TextSendMessage 
line_bot_api = None
with open("secret.json", "r") as f:
    secret = json.load(f)
    access_token = secret["line_bot_channel_access_token"]
    line_bot_api = LineBotApi(access_token)
f.close()

f = open("./Grader/README.md", 'w', encoding="utf-8")

# write header
f.write("# Grader problem list\n")

# get problem info
problem_dict = get_problem_info()

#  loop to collect find name of problem in Grader folder
dict_code = {}
for file in os.listdir("./Grader"):
    if not file.endswith(".exe") and not file.endswith(".md"):
        name = file
        # get last time modified
        time_ = (os.path.getmtime("./Grader/" + file))
        dict_code[name] = [0,time_]
# sort all by last time modified
code_list = sorted(dict_code, key=lambda x: dict_code[x][1], reverse=True)
# stat problem list table
f.write("## Statistics\n\n")
f.write("| Language | Amount | Solved | Unsolved | Total Score\n")
f.write("| :---: | :---: | :---: | :---: | :---: |\n")
# C lang
num_c = 0
num_solved_c = 0
num_score_c = 0
for code in code_list:
    if code.endswith(".c"):
        num_c += 1
        sc = int(problem_dict[code.split(".")[0]]["score_text"].split(" ")[0])
        if sc == 100:
            num_solved_c += 1
        num_score_c += int(sc)
# C++ lang
num_cpp = 0
num_solved_cpp = 0
num_score_cpp = 0
for code in code_list:
    if code.endswith(".cpp"):
        num_cpp += 1
        try:
            sc = int(problem_dict[code.split(".")[0]]["score_text"].split(" ")[0])
        except:
            sc = 0
        if sc == 100:
            num_solved_cpp += 1
        num_score_cpp += int(sc)
# Python lang
num_py = 0
num_solved_py = 0
num_score_py = 0
for code in code_list:
    if code.endswith(".py"):
        num_py += 1
        try:
            sc = int(problem_dict[code.split(".")[0]]["score_text"].split(" ")[0])
        except:
            sc = 0
        if sc == 100:
            num_solved_py += 1
        num_score_py += int(sc)
# Print by most score come first
num_all = [num_c, num_cpp, num_py]
num_solved_all = [num_solved_c, num_solved_cpp, num_solved_py]
num_score_all = [num_score_c, num_score_cpp, num_score_py]
lang = ["C", "C++", "Python"]
# sort by score
for i in range(3):
    for j in range(i, 3):
        if num_score_all[i] < num_score_all[j]:
            num_score_all[i], num_score_all[j] = num_score_all[j], num_score_all[i]
            num_solved_all[i], num_solved_all[j] = num_solved_all[j], num_solved_all[i]
            num_all[i], num_all[j] = num_all[j], num_all[i]
            lang[i], lang[j] = lang[j], lang[i]
# print table
for i in range(3):
    f.write("| " + lang[i] + " | " + str(num_all[i]) + " | " + str(num_solved_all[i]) + " | " +
            str(num_all[i] - num_solved_all[i]) + " | " + str(num_score_all[i]) + " |\n")
# total
f.write("| **Total** | **" + str(num_c + num_cpp + num_py) + "**|**" + str(num_solved_c + num_solved_cpp + num_solved_py) + "** | **" + str(num_c +
        num_cpp + num_py - num_solved_c - num_solved_cpp - num_solved_py) + "**| **" + str(num_score_c + num_score_cpp + num_score_py) + "** |\n")
f.write("\n")

# suggest for search
f.write('<u>**Suggest to search by the name that on table**</u>\n\n')

# print summary table
f.write("## Problem List\n\n")
f.write("| Problem | Problem name| Score | Language | Last modified |\n")
f.write("|---------|-------------|-------|----------|---------------|\n")
for code in code_list:
    # file type c/c++ or python
    file_type = ""
    if code.endswith(".py"):
        file_type = "Python"
    elif code.endswith(".cpp"):
        file_type = "C++"
    elif code.endswith(".c"):
        file_type = "C"
    try:
        name = problem_dict[code.split(".")[0]]["task_name"]
    except:
        name = ''
    # write to file
    try:
        print(f'| [{code.split(".")[0]}]({code}) | {(name)} | {problem_dict[code.split(".")[0]]["score_text"]} | {file_type} | {problem_dict[code.split(".")[0]]["last_grade_date"]} |', file=f)
    except:
        continue
f.write("\n")
# write update time in format dd-mm-yyyy hh:mm
f.write(f'Last update : {datetime.datetime.now().strftime("%d-%m-%Y %H:%M")}\n')
f.close()

# append to log with time stamp
this_name = os.path.basename(__file__)
with open('log.log', 'a') as f:
    print(f'{this_name} : {datetime.datetime.now()}', file=f)
    print(f'Number of problem : {len(code_list)}', file=f)
    print(f'Number of C problem : {num_c}', file=f)
    print(f'Number of C++ problem : {num_cpp}', file=f)
    print(f'Number of Python problem : {num_py}', file=f)
    print(f'Number of solved problem : {num_solved_c + num_solved_cpp + num_solved_py}', file=f)
    print(f'Number of unsolved problem : {num_c + num_cpp + num_py - num_solved_c - num_solved_cpp - num_solved_py}', file=f)
    print('', file=f)

# send message to line
if line_bot_api != None:
    message = f'Update problem list in grader\n'
    message += f'Number of problem : {len(code_list)}\n'
    message += f'Number of C problem : {num_c}\n'
    message += f'Number of C++ problem : {num_cpp}\n'
    message += f'Number of Python problem : {num_py}\n'
    message += f'Number of solved problem : {num_solved_c + num_solved_cpp + num_solved_py}\n'
    message += f'Number of unsolved problem : {num_c + num_cpp + num_py - num_solved_c - num_solved_cpp - num_solved_py}\n'
    line_user_id = r'U6277d126256566afc767481bbd0a10b9'
    line_bot_api.push_message(line_user_id, TextSendMessage(text=message[:-1]))