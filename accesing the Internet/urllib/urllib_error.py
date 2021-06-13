'''
urllin contains modules for working with URLs:
- urllib.request
- urlib.error
- urllib.parse
- urllib.robotparser

'''

# using urllib to request data
import urllib.request
from http import HTTPStatus
from urllib.error import HTTPError, URLError 

def main():
    url = "http://no-such-server.org"       # will generate a URLError
    #url = "http://httpbin.org/status/404"   # will generate a HTTPError
    #url = "http://httpbin.org/html"         # should work without errors

    # Issue the request with the data params as part of the url
    try:
        result = urllib.request.urlopen(url)
        # print the result
        print("Result code: {0}".format(result.status))
        if(result.getcode() == HTTPStatus.OK):
            print("Returned data: --------------------")
            print(result.read().decode('utf-8'))
    except HTTPError as err:
        print("Error: {0}".format(err.code))
    except URLError as err:
        print("Yeah that server is bunk. {0}".format(err.reason))

if __name__ == "__main__":
    main()    
