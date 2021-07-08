# https://findwork.dev/blog/advanced-usage-python-requests-timeouts-retries-hooks/

import requests

'''
(1) Request hooks
Requests offers the shorthand helper raise_for_status() which asserts that the 
response HTTP status code is not a 4xx or a 5xx, i.e that the request didn't result 
in a client or a server error.
'''
# response = requests.get('https://api.github.com/user/repos?page=1')
# # Assert that there were no errors
# response.raise_for_status()

'''
The above can get repetitive if you need to raise_for_status() for each call. Luckily 
the requests library offers a 'hooks' interface where you can attach callbacks on certain 
parts of the request process. We can use hooks to ensure raise_for_status() is 
called for each response object.
'''
# Create a custom requests object, modifying the global module throws an error
http = requests.Session()

assert_status_hook = lambda response, *args, **kwargs: response.raise_for_status()
http.hooks["response"] = [assert_status_hook]

http.get("https://api.github.com/user/repos?page=1")

