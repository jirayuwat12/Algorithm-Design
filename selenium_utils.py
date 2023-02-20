# selenuim
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json

# username and password
f = open("secret.json", "r")
secret = json.loads(f.read())
const_username = secret["username"]
const_password = secret["password"]

f.close()
# opne in headless mode with edge
options = webdriver.EdgeOptions()
options.add_argument("headless")
driver = webdriver.Edge(options=options)
driver.get("https://nattee.net/grader/main/list")
# get username and password
username = driver.find_element(By.NAME, "login")
password = driver.find_element(By.NAME, "password")
username.send_keys(const_username)
password.send_keys(const_password)

# submit
driver.find_element(By.NAME, "commit").click()


def get_problem_info():
    # get problem table that class table table-striped table-condensed
    table = driver.find_element(By.CLASS_NAME, "table-striped")
    # get all problem
    problems = table.find_elements(By.TAG_NAME, "tr")
    ret = dict()
    for problem in problems[1:]:
        try:
            [header,grade_date,score,_] = problem.text.split("\n")
        except:
            continue
        task_id = header.split(" ")[0]
        task_name = " ".join(header.split(" ")[1:])
        number_grade = int(score.split(" ")[1])
        last_grade_date = " ".join(grade_date.split(" ")[4:])
        score_text = " ".join(score.split(" ")[1:])
        # print(task_id,task_name,number_grade,last_grade_date,score_text)
        ret[task_id] = {
            "task_name": task_name,
            "number_grade": number_grade,
            "last_grade_date": last_grade_date,
            "score_text": score_text
        }
    return ret
if __name__ == "__main__":
    print(get_problem_info())