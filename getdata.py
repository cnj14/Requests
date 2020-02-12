# getdata.py

import requests

print("GETTING SOME DATA FROM THE INTERNET...")

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/1.json"
print("URL: ", request_url)

response = requests.get(request_url)
print(type(response))
# print(dir(response))

print(response.status_code)
print(response.text)

breakpoint()

