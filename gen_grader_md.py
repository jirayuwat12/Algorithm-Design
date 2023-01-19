import os
import time

f = open("./Grader/grader.md",'w')  

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
# stat problem list
f.write("## Statistic\n\n")
f.write("- Total problem : " + str(len(code_list)) + "\n\n")
f.write("- Total score : " + str(sum([int(dict_code[code][0]) for code in code_list])) + "\n\n")
# print summary table
f.write("| Problem | Score | Last modified |\n")
f.write("| :---: | :---: | :---: |\n")
# make name is kyper link to code
for code in code_list:
    f.write("| [" + code.split('.')[0] + "](" + code + ") | " + dict_code[code][0] + " | " + time.strftime("%a %d/%m/%Y %H:%M", time.localtime(dict_code[code][1])) + " |\n")
f.write("\n")
