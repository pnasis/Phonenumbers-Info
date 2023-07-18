import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import opencage
from opencage.geocoder import OpenCageGeocode

mobileNo = input("Enter Mobile Number with Country code: ")
mobileNo = phonenumbers.parse(mobileNo)


# Getting carrier of a phone number
print(carrier.name_for_number(mobileNo, "en"))

# get timezone a phone number
print(timezone.time_zones_for_number(mobileNo))

# Getting region information
print(geocoder.description_for_number(mobileNo, "en"))

key = 'b3e11918ebc6439fb5a921bc7b19d6ed'
geocoder = OpenCageGeocode(key)
location = geocoder.description_for_number(mobileNo, "en")
query = str(location)
results = geocoder.geocode(query)
print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print("Latitude: %s Longitude: %s" % (lat, lng))

# Validating a phone number
print("Valid Mobile Number: ", phonenumbers.is_valid_number(mobileNo))

# Checking possibility of a number
print("Checking possibility of Number: ", phonenumbers.is_possible_number(mobileNo))
