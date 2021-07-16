"""Python-decouple
- pip install python-decouple

Decouple always searches for Options in this order:
- Environment variables;
- Repository: ini or .env file;
- default argument passed to config.
"""

from decouple import config

# Read settings
SECRET_KEY = config('SECRET_KEY')
print(SECRET_KEY)
