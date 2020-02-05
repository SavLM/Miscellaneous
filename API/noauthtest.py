# Using Open Notify API, which gives info about the ISS
# Doesn't require authentication

# remember to pip install requests
import requests
# request from api endpoint that doesn't exist
response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
# should return 404
print(response.status_code)
