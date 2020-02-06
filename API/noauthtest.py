## Using Open Notify API, which gives info about the ISS
##   Doesn't require authentication

## remember to pip install requests
import requests
import json
from datetime import datetime

## request from api endpoint that doesn't exist
#response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
## should return 404
#print(response.status_code)

## endpoint that takes no input
##   returns json response
#response = requests.get("http://api.open-notify.org/astros.json")
#print(response.status_code)
#with open('astros.json', 'w') as f:
#    json.dump(response.json(), f, sort_keys=True, indent=4)

## pulls response output from output.json (so I don't have to keep making request during testing)
#with open('astros.json') as f:
#    response = json.load(f)
#print(json.dumps(response, sort_keys=True, indent=4))

## request that requires parameters
##   this one needs a latitude and longitude to return when the iss will pass over that location next
##   could also do http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74
parameters = {
    "lat": 37.5,
    "lon": -77.5
}
#response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
#print(response.status_code)
#with open('iss-pass.json', 'w') as f:
#    json.dump(response.json()['response'], f, indent=4)

with open('iss-pass.json') as f:
    times = json.load(f)
print(json.dumps(times, indent=4))

## times returned in timestamp format,
##   so need to use datetime.fromtimestamp() method
risetimes = []
for t in times:
    rt = t['risetime']
    st = rt + t['duration']
    risetimes.append({ "rise": datetime.fromtimestamp(rt), "set": datetime.fromtimestamp(st) })
for t in risetimes:
    print("Rises at ", t["rise"], " and sets at ", t["set"])
