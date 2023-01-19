import os
import time

f = open("./Grader/README.md",'w')  

# write header
f.write("# Grader problem list\n")

#  loop to collect find name of problem in Grader folder

dict_code = {}
for file in os.listdir("./Grader"):
    if not file.endswith(".exe") and not file.endswith(".md"):
        name = file
        # get score
        with open("./Grader/" + file, 'r') as f2:
            score = (f2.readline().split(' ')[1].strip())
        # get last time modified
        time_ = (os.path.getmtime("./Grader/" + file))
        dict_code[name] = [score, time_]
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
        if dict_code[code][0] == "100":
            num_solved_c += 1
        num_score_c += int(dict_code[code][0])
# C++ lang
num_cpp = 0
num_solved_cpp = 0
num_score_cpp = 0
for code in code_list:
    if code.endswith(".cpp"):
        num_cpp += 1
        if dict_code[code][0] == "100":
            num_solved_cpp += 1
        num_score_cpp += int(dict_code[code][0])
# Python lang
num_py = 0
num_solved_py = 0
num_score_py = 0
for code in code_list:
    if code.endswith(".py"):
        num_py += 1
        if dict_code[code][0] == "100":
            num_solved_py += 1
        num_score_py += int(dict_code[code][0])
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
    f.write("| " + lang[i] + " | " + str(num_all[i]) + " | " + str(num_solved_all[i]) + " | " + str(num_all[i] - num_solved_all[i]) + " | " + str(num_score_all[i]) + " |\n")
# total
f.write("| **Total** | **" + str(num_c + num_cpp + num_py) + "**|**" + str(num_solved_c + num_solved_cpp + num_solved_py) + "** | **" + str(num_c + num_cpp + num_py - num_solved_c - num_solved_cpp - num_solved_py) + "**| **" + str(num_score_c + num_score_cpp + num_score_py) + "** |\n")
f.write("\n")

# suggest for search
f.write('<u>**Suggest to search by the name that on table**</u>\n\n')

# print summary table
f.write("## Problem List\n\n")
f.write("| Problem | Score | Language | Last modified |\n")
f.write("| :---: | :---: | :---: | :---: |\n")
for code in code_list:
    # date in format day of week day month year(only last 2 digit) hour:minute
    date = time.strftime("%a %d %b %y %H:%M", time.localtime(dict_code[code][1]))    
    # file type c/c++ or python
    file_type = ""
    if code.endswith(".py"):
        file_type = "Python"
    elif code.endswith(".cpp"):
        file_type = "C++"
    elif code.endswith(".c"):
        file_type = "C"
    # write to file
    f.write("| [" + code + "](./" + code + ") | " + dict_code[code][0] + " | " + file_type + " | " + date + " |\n")
f.write("\n")
f.close()

# append to log with time stamp
import datetime
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