# using the requests library to access internet data

import requests
import json

def main():
    # Use requests to issue a standard HTTP get request
    url = 'http://httpbin.org/json'
    result = requests.get(url)

    # use the built in JSON function to return parsed data
    dataobj = result.json()
    print(json.dumps(dataobj, indent=4))

    # Access data in the python object
    print(list(dataobj.keys()))
    
    print(dataobj['slideshow']['title'])
    num_slides = len(dataobj['slideshow']['slides'])
    print(f'There are { num_slides } slides')


if __name__ == "__main__":
    main()