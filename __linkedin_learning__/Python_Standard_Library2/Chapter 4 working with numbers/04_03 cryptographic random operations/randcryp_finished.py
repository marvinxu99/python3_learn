# Using cryptographic-appropriate methods to generate random data
# that may be sensitive. secrets module introduced in Python 3.6
import os
import secrets


# the urandom() function in the OS module produces random numbers that
# are cryptographically safe to use for sensitive purposes
result = os.urandom(8)
print([hex(b) for b in result])


# secrets.choice is the same as random.choice but more secure
moves = ["rock", "paper", "scissors"]
print(secrets.choice(moves))


# secrets.token_bytes generates random bytes
result = secrets.token_bytes()
print(result)


# secrets.token_hex creates a random string in hexadecimal
result = secrets.token_hex()
print(result)


# secrets.token_urlsafe generates characters that can be in URLs
result = secrets.token_urlsafe()
print(result)
