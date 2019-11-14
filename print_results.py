import datetime

"""
Parse and print ISS pass information
Parameters: index - the index of the json information we are on
			iss_pass_times - ISS pass time information to be parsed
"""
def print_ISS_pass_info(index, iss_pass_times):
	# Convert risetime to normal date format
	date = datetime.datetime.fromtimestamp(iss_pass_times[index]["risetime"])
	date = date.strftime('%Y-%m-%d %H:%M:%S')
	# Get the duration
	duration_in_minutes = iss_pass_times[index]["duration"]/60
	# Print the risetime and duration for that pass
	print("Risetime " + str(index+1) + ": " + date + "\n    Duration: " + str(duration_in_minutes) + " minutes.")