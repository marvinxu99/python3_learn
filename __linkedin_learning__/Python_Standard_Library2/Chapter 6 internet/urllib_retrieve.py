# retrieve data from the internet
import urllib.request


sample_url = "http://httpbin.org/xml"

# TODO: Create a request to retrieve data using urllib.request
resp = urllib.request.urlopen(sample_url)

# TODO: Check the status
status_code = resp.status
print(status_code)

# TODO: if no error, then read the response contents
if status_code >= 200 and status_code < 300:
    # TODO: work with response headers
    print(resp.getheaders())
    print(resp.getheader('Content-Length'))
    print(resp.headers['Content-Type'])

    # TODO: read the data from the URL
    data = resp.read().decode("utf-8")
    print(data)
