@REM run gen_codeforces_md.py via python
@REM Path: gen_codeforces_md.py

@echo off
@echo ----------------------------------------

python gen_codeforces_md.py
@echo [LOG] gen_codeforces_md.py finished
@echo ----------------------------------------

python ./Utils/delete_exe.py
@echo [LOG] ./Utils/delete_exe.py finished
@echo ----------------------------------------

@echo [LOG] update_sub_md.bat finished