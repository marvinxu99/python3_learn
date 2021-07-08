# Python Essential Libraries by Joe Marini course example
# Example file for using Requests library
import requests

# TODO: use a timeout value for a request
resp = requests.get("https://httpbin.org/delay/0.5", timeout=1.0)
# resp = requests.get("https://httpbin.org/delay/2.5", timeout=1.0)
print(resp.status_code)

# TODO: introspect the redirection history
resp = requests.get("http://github.com")
print(resp.url)
print(resp.history, type(resp.history))
orig = resp.history.pop()
print(type(orig))
print(orig.status_code)
print(orig.url)
print(orig.reason)
'''
https://github.com/
[<Response [301]>] <class 'list'>
<class 'requests.models.Response'>
301
http://github.com/
Moved Permanently
'''

# TODO: Use a session object to group requests and settings
sess = requests.Session()
# sess.get("https://httpbin.org/cookies/set/sample/123456789")
# sess.get('https://httpbin.org/cookies/get/sample/')
# print(resp.text)

sess.headers.update({
    "User-Agent": "Mozilla/5.0 (X11, Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 FireFox/68.0"
})
resp = sess.get("http://google.ca")
print(len(resp.content))

sess.headers.update({
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B329 Safari/8536.25"
})
resp = sess.get("http://google.ca")
print(len(resp.content))