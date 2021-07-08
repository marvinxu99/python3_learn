'''
urllin contains modules for working with URLs:
- urllib.request
- urlib.error
- urllib.parse
- urllib.robotparser

'''

# using urllib to request data
import urllib.request

def main():
    url = "http://httpbin.org/xml"

    # open the url
    result = urllib.request.urlopen(url)

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
