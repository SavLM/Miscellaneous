## Working with Last.fm API

import requests
import json
import time

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def jloadfile(obj, fname):
    with open(fname, 'w') as f:
        json.dump(obj, f, indent=4)

## Need to look at API guidelines in documentation

## API Key is like a password for using API, used to authenticate yourself
## Create an api account and grab API Key
API_KEY = 'xxxxxxxxxx'

## Identify yourself using headers
## Last.fm uses user-agent to identify
## using headers parameter from the requests library with a dict of headers
USER_AGENT = 'Savleighm'
def lastfm_get(payload):
    headers = { 'user-agent': USER_AGENT }
    url = 'http://ws.audioscrobbler.com/2.0/'
    payload['api_key'] = API_KEY
    payload['format'] = 'json'
    response = requests.get(url, headers=headers, params=payload)
    return response

## only 1 real endpoint, so each “endpoint” is actually specified by using the method parameter.
## chart.getTopArtists endpoint for dataset of popular artists
#r = lastfm_get({'method': 'chart.gettopartists'})

## gives first 50 artists
#print(r.status_code)
#jprint(r.json())
#jloadfile(r.json(), 'lastfm.json')

## Given @attr to keep track of pages
##      "@attr": {
##      "page": "1",
##      "perPage": "50",
##      "totalPages": "61010",
##      "total": "3050495"
##      }
## Use limit parameter to get more results per page

## Rate limiting to avoid being banned
## use time.sleep(seconds) function
## Can also use a request cache
##  don't need to make unnecessary, extra API calls
##  don't need to rate limit repeated calls from the cache
##      remember pip install requests-cache
#       import requests_cache
#       requests_cache.instal_cache()

responses = []
page = 1
total_pages = 99999 # this is just a dummy number so the loop starts

while page <= total_pages:
    payload = {
        'method': 'chart.gettopartists',
        'limit': 500,
        'page': page
    }

    # print some output so we can see the status
    print("Requesting page {}/{}".format(page, total_pages))

    # make the API call
    response = lastfm_get(payload)

    # if we get an error, print the response and halt the loop
    if response.status_code != 200:
        print(response.text)
        break

    # extract pagination info
    page = int(response.json()['artists']['@attr']['page'])
    total_pages = int(response.json()['artists']['@attr']['totalPages'])

    # append response
    responses.append(response)

    # if it's not a cached result, sleep
    if not getattr(response, 'from_cache', False):
        time.sleep(0.25)

    # increment the page number
    page += 1
