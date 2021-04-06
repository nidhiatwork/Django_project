import requests

import requests
# Making a GET request
r = requests.get('https://api.github.com')

# check status code for response received
# success code - 200
print(r.json())

# print content of request
# print(r.content)
