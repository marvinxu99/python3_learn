# https://findwork.dev/blog/advanced-usage-python-requests-timeouts-retries-hooks/

import requests

response = requests.get('https://api.github.com/user/repos?page=1')

print(response.json())

# Assert that there were no errors
response.raise_for_status()

