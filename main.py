from api import get_iss_pass_times, get_longitude, get_latitude
from input_validation import is_valid_latitude, is_valid_longitude

# Accept latitude input and validate
latitude = raw_input("\nEnter your current latitude: ")
while(is_valid_latitude(latitude) == False):
	latitude = raw_input("\nInvalid latitude. Try again: ")

# Accept longitude input and validate
longitude = raw_input("Enter your current longitude: ")
while(is_valid_longitude(longitude) == False):
	longitude = raw_input("\nInvalid longitude. Try again: ")

iss_pass_times = get_iss_pass_times(latitude, longitude)

# Retrieve and store current latitude and longitude values of the ISS
ISS_longitude = get_longitude()
ISS_latitude = get_latitude()

print
print(iss_pass_times)
print("\nCurrent ISS coordinates: {}, {}".format(ISS_latitude, ISS_longitude))
