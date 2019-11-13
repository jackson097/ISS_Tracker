import requests
import json

"""
"""
def get_iss_information(latitude, longitude):
	return requests.get("http://api.open-notify.org/iss-pass.json?lat=latitude&lon=longitude").json()


"""
def jprint(obj):
    # Create a formatted string of the JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

latitude_and_longitude = {
	"lat": 40.71,
	"lon": -74
}

response = requests.get("http://api.open-notify.org/iss-pass.json", params=latitude_and_longitude)

jprint(response.json())
"""