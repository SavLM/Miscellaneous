# Using Open Notify API, which gives info about the ISS
# Doesn't require authentication

# remember to pip install requests
import requests
import json
# request from api endpoint that doesn't exist
#response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
# should return 404
#print(response.status_code)

# endpoint that takes no input
# returns json response
response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
#print(response.json())
with open('output.json', 'w') as f:
    json.dump(response.json(), f, indent=2)
