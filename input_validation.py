"""
Check if the coordinate provided is a valid coordinate for the API call
Parameters: type - latitude or longitude
			coordinate - coordinate value passed as a string
Returns: boolean - True if the coordinate is valid, Else False
"""
def _is_valid_coordinate(type, coordinate):
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
  		coordinate = float(coordinate)
	except:
  		return False

	# Validate the coordinates are within allowed values
	if coordinate > value or coordinate < (value-value*2):
		return False
	return True


"""
Checks if coordinate is a valid longitude value
Parameters: coordinate - The longitude coordinate to be validated (string)
Returns: True if longitude is valid, Else False
"""
def is_valid_longitude(coordinate):
	return _is_valid_coordinate("longitude", coordinate)

"""
Checks if coordinate is a valid latitude value
Parameters: coordinate - The latitude coordinate to be validated (string)
Returns: True if latitude is valid, Else False
"""
def is_valid_latitude(coordinate):
	return _is_valid_coordinate("latitude", coordinate)