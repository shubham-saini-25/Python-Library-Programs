# Required Module:- pip install Faker

# import the Faker liberary
from faker import Faker

# Assign Faker() to a variable
fake = Faker()

# Generate and Print Fake Name
print("Name\t:", fake.name())

# Generate and Print Fake Email
print("Email\t:", fake.email())

# Generate and Print Fake Address
print("Address\t:", fake.address())

# Generate and Print Fake Country
print("Country\t:", fake.country())

# Generate and Print Fake Company
print("Company\t:", fake.company())