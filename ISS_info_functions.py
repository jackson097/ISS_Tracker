import datetime

"""
Extract the date from the json response
Parameters: index - the current index of the json response
			iss_pass_times - json iss pass time info
Returns: date - formatted date of iss pass
"""
def _get_date(index, iss_pass_times):
	try:
		date = datetime.datetime.fromtimestamp(iss_pass_times[index]["risetime"])
		date = date.strftime('%Y-%m-%d %H:%M:%S')
		return date
	except:
		print("\nAn error has occured. Cannot parse date.")
		print("Ending program...")
		exit(0)
	
"""
Extract the duration from the json response
Parameters: index - the current index of the json response
			iss_pass_times - json iss pass time info
Returns: duration - formatted duration of iss pass
"""
def _get_duration(index, iss_pass_times):
	try:
		duration_in_minutes = iss_pass_times[index]["duration"]/60
		return duration_in_minutes
	except:
		print("\nAn error has occured. Cannot find duration.")
		print("Ending program...")
		exit(0)

"""
Parse and print ISS pass information
Parameters: index - the index of the json information we are on
			iss_pass_times - ISS pass time information to be parsed
"""
def print_ISS_pass_info(index, iss_pass_times):
	# Convert risetime to normal date format
	date = _get_date(index, iss_pass_times)
	# Get the duration
	duration_in_minutes = _get_duration(index, iss_pass_times)
	# Print the risetime and duration for that pass
	print("Risetime " + str(index+1) + ": " + date + "\n    Duration: " + str(duration_in_minutes) + " minutes.")
	return