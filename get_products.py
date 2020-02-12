# get_products.py

import requests
import json 

print("GETTING SOME DATA FROM THE INTERNET...")

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
print("URL: ", request_url)

response = requests.get(request_url)
print(type(response))
# print(dir(response))

# print(response.status_code)
# print(response.text)

parsed_response = json.loads(response.text)
print(type(parsed_response))

for d in parsed_response:
    print(d["id"], d["name"])
# print(parsed_response["name"])


# breakpoint()
