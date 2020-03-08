# Python program to explain os.environ object 

# importing os module 
import os 
import pprint 

# Get the list of user's 
# environment variables 
env_var = os.environ 

# Print the list of user's 
# environment variables 
print("User's Environment variable:") 
pprint.pprint(dict(env_var), width = 1) 

print("OS:", end=' ') 
pprint.pprint(env_var.get('OS'))

print("HOMEDRIVE:", end=' ') 
pprint.pprint(env_var['HOMEDRIVE'])

if 'HOME' in env_var:
	print("'HOME' is included in os.environ")
else:
	print("'HOME' is not included in os.environ")

if 'HOMEDRIVE' in env_var:
	print("'HOMEDRIVE' is included in os.environ")
else:
	print("'HOMEDRIVE' is not included in os.environ")
	
# os.getlogin()
print('Hello, ' + os.getlogin() + '! How are you?')