import requests
import json

"""
Returns current ISS information in JSON format relative to your position on Earth
Parameters: latitude - your current latitude
		 longitude - your current longitude
Returns: json_results - results of API call in json format
"""
def get_iss_pass_times(latitude, longitude):
	try:
		json_results = requests.get("http://api.open-notify.org/iss-pass.json?lat=" + latitude + "&lon=" + longitude).json()["response"]
	except:
		print("\nThere was an issue retrieving ISS statistics.")
		print("Ending program...")
		exit(0)
	return json_results
	
"""
Returns the current coordinates of the ISS in JSON form
"""
def _get_iss_coordinates():
	try:
		iss_coordinates = requests.get("http://api.open-notify.org/iss-now.json").json()
	except:
		print("\nThere was an issue retrieving ISS coordinates.")
		print("Ending program...")
		exit(0)
	return iss_coordinates
	
"""
Returns the longitude value of the ISS
"""
def get_longitude():
	return _get_iss_coordinates()['iss_position']['longitude']
	
"""
Returns the latitude value of the ISS
"""
def get_latitude():
	return _get_iss_coordinates()['iss_position']['latitude']