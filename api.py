import requests
import json

"""
Returns current ISS information in JSON format relative to your position on Earth
Parameters: latitude  - your current latitude
		 longitude - your current longitude
"""
def get_iss_pass_times(latitude, longitude):
	return requests.get("http://api.open-notify.org/iss-pass.json?lat=" + latitude + "&lon=" + longitude).json()
	
"""
Returns the current coordinates of the ISS in JSON form
"""
def get_iss_coordinates():
	return requests.get("http://api.open-notify.org/iss-now.json").json()
	
"""
"""
def get_longitude():
	return get_iss_coordinates()['iss_position']['longitude']
	
"""
"""
def get_latitude():
	return get_iss_coordinates()['iss_position']['latitude']