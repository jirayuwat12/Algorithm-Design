@REM  delete all *.exe file in grader and codeforces folder
python ./Utils/delete_exe.py

@REM  update REAADME.md

python gen_codeforces_md.py
python gen_grader_md.py

@REM  push to github

git add .
git commit -m "update"

git push 

@REM Path: pull_github.bat