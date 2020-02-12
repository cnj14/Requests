# get_grades.py

import requests
import json 

print("GETTING SOME DATA FROM THE INTERNET...")

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
print("URL: ", request_url)

response = requests.get(request_url)
parsed_response = json.loads(response.text)
print(type(parsed_response))

all_grades = []
for student in parsed_response["students"]:
    grade = student["finalGrade"]
    all_grades.append(grade)

# print(all_grades)

total = sum(all_grades)

average = (total/len(all_grades))
average = "{0:.2f}".format(average)
high_score = (max(all_grades))
high_score = "{0:.1f}".format(high_score)
low_score = (min(all_grades))
low_score = "{0:.1f}".format(low_score)

print("CLASS AVERAGE: ", average)
print("MAX SCORE: ", high_score)
print("MIN SCORE: ", low_score)


