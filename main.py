from api import get_iss_information

# Take inputs
latitude = input("Enter your current latitude :")
longitude = input("Enter your current longitude :")

print(get_iss_information(float(latitude), float(longitude)))

##### ADD VALIDATION