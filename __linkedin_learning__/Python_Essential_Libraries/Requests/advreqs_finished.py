# Python Essential Libraries by Joe Marini course example
# Example file for using Requests library
import requests

# TODO: use a timeout value for a request
resp = requests.get("https://httpbin.org/delay/0.5", timeout=1.0)
print(resp.status_code)

# TODO: introspect the redirection history
resp = requests.get("http://github.com")
print(resp.url)
print(resp.history)
orig = resp.history.pop()
print(orig.status_code)
print(orig.url)
print(orig.reason)

# TODO: Use a session object to group requests and settings
# create the session
sess = requests.Session()
# use the session to persist a cookie across requests
sess.get('https://httpbin.org/cookies/set/sample/123456789')
resp = sess.get('https://httpbin.org/cookies')
print(resp.text)

# Customize the user-agent to simulate different browsers
# Set the user-agent to be Firefox
sess.headers.update({
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
})
resp = sess.get("http://google.com")
print(len(resp.content))

# Set the user-agent to be an iPhone
sess.headers.update({
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) relesys_web_client/1.3.10.0 (RelesysApp/1.3.43 net.relesysapp.nettoenterprise)"
})
resp = sess.get("http://google.com")
print(len(resp.content))
