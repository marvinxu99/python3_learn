# Python Essential Libraries by Joe Marini course example
# Example file for the Requests library
import requests

# define user and password values
user = "theuser"
passwd = "thepass"

# TODO: use the basic authentication method
url = 'https://httpbin.org/basic-auth/theuser/thepass'
resp = requests.get(url, auth=(user, passwd))
print(resp.status_code)
print(resp.text)

# TODO: use the digest authentication method