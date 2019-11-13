from api import get_iss_pass_times, get_longitude, get_latitude

# Take inputs
latitude = raw_input("\nEnter your current latitude: ")
longitude = raw_input("Enter your current longitude: ")

iss_pass_times = get_iss_pass_times(latitude, longitude)

longitude = get_longitude()
latitude = get_latitude()

print
print(iss_pass_times)
print
print("Latitude = {}".format(latitude))
print("Longitude = {}".format(longitude))