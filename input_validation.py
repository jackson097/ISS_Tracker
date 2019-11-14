### Latitude must be between -90.0 and 90.0
### Latitude must be between -180.0 and 180.0


"""
Check if the coordinate provided is a valid coordinate for the API call
Parameters: type       - latitude or longitude
			coordinate - coordinate value passed as a string
"""
def is_valid_coordinate(type, coordinate):
	# Determine what the max/min coordinates are by the type
	if type == "longitude":
		value = 180
	elif type == "latitude":
		value = 90
	else:
		print("Something went wrong... Ending program.")
		exit(0)

	# Validate that the coordinate is an integer
	try:
  		coordinate = int(coordinate)
	except:
  		return False

	# Validate the coordinates are within allowed values
	if coordinate > value or coordinate < (value-value*2):
		return False
	return True


"""
Checks if coordinate is a valid longitude value
Parameters: coordinate - The longitude coordinate to be validated (string)
"""
def is_valid_longitude(coordinate):
	return is_valid_coordinate("longitude", coordinate)

"""
Checks if coordinate is a valid latitude value
Parameters: coordinate - The latitude coordinate to be validated (string)
"""
def is_valid_latitude(coordinate):
	return is_valid_coordinate("latitude", coordinate)