from api import get_iss_pass_times, get_longitude, get_latitude
from input_validation import is_valid_latitude, is_valid_longitude
from print_results import print_ISS_pass_info

print("Enter a longitude and latitude to see ISS pass information over those coordinates.")

# Retrieve and store current latitude and longitude values of the ISS
ISS_longitude = get_longitude()
ISS_latitude = get_latitude()

# Print the current coordinates of the ISS
print("\nCurrent ISS coordinates: {}, {}".format(ISS_latitude, ISS_longitude))

# Accept latitude input and validate
latitude = raw_input("\nEnter latitude: ")
while(is_valid_latitude(latitude) == False):
	latitude = raw_input("\nInvalid latitude. Try again: ")

# Accept longitude input and validate
longitude = raw_input("Enter longitude: ")
while(is_valid_longitude(longitude) == False):
	longitude = raw_input("\nInvalid longitude. Try again: ")

# Print the ISS pass times over the location provided
print("\nISS passes over (" + latitude + "," + longitude + "):")
iss_pass_times = get_iss_pass_times(latitude, longitude)
for index in range(0, len(iss_pass_times)-1):
	print_ISS_pass_info(index, iss_pass_times)