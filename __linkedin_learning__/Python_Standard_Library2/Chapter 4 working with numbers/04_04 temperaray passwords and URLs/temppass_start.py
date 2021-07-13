# Create a temporary password using Python
import secrets
import string


# TODO: Function to return a temporary password given a length
def generateTempPass(numChars=8):
    potential_chars = string.ascii_letters + string.digits + "=-&?/!@#$%*"
    result = ''.join(secrets.choice(potential_chars) for _ in range(numChars))
    print(result)

# TODO: Function to return a temporary password and enforce 1 number and 1 uppercase
def generateBetterPass(numChars=8):
    potential_chars = string.ascii_letters + string.digits + "=-&?/!@#$%*"
    while True:
        result = ''.join(secrets.choice(potential_chars) for _ in range(numChars))
        if (any(c.isupper() for c in result) 
                and any(c.isdigit() for c in result)):
            break    
    return result

# create a temporary password
print(generateTempPass(10))

# create a stronger temporary password
print(generateBetterPass(10))


# TODO: create a temporary, hard-to-guess URL
resultUrl = "https://my.example.com?reset="
resultUrl += secrets.token_urlsafe(15)
print(resultUrl)
