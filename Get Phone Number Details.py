# Required Module:- pip install phonenumbers

import phonenumbers

from phonenumbers import carrier

# Enter Country code before Your no.
# like "+917676767676"
mob = input("Enter Your Phone Number: ")

service = phonenumbers.parse(mob)

print(carrier.name_for_number(service, "en"))