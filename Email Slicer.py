# Email Slicer using Python

# input the email 
email = input("Enter your Email adress: ").strip()

# Slice out the user name
user_name = email[:email.index("@")]

# Slice out the domain name
domain_name = email[email.index("@") + 1:]

slice_data = f"Your username is: {user_name} \nYour domain name is: {domain_name}"

# Display the result message
print(slice_data)

# Output:-
# Enter your Email adress: sainishuham915@gmail.com
# Your username is: sainishuham915
# Your domain name is: gmail.com