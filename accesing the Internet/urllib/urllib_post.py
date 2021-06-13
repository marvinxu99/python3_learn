'''
urllin contains modules for working with URLs:
- urllib.request
- urlib.error
- urllib.parse
- urllib.robotparser

'''

# using urllib to request data
import urllib.request
import urllib.parse

def main():
    url = "http://httpbin.org/post"

    # Create some data to pass to the GET request
    args = {
        "name": "marvin xu",
        "is_author": True
    }

    # The data needs to be url-encoded before passing as arguments
    data = urllib.parse.urlencode(args)

    data = data.encode()   # default is UTF-8

    # Issue the request with the data params as part of the url
    result = urllib.request.urlopen(url, data=data)

    # print the result
    print("Result code: {0}".format(result.status))

    # print the returned data header
    print("Headers: --------------------") 
    print(result.getheaders())

    # print the returned data itself
    print("Returned data: --------------------")
    print(result.read().decode('utf-8'))


if __name__ == "__main__":
    main()    
