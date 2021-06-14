import requests
from requests import HTTPError, Timeout

def main():

    # url = "http://httpbin.org/get"
    # url = "http://httpbin.org/status/404"
    url = "http://httpbin.org/delay/5"

    # some parameters to the URL via a GET request
    # Note that requests handles this for you, no manual encoding
    dataValues = {
        "key1": "value1",
        "key2": "value2"
    }

    try: 
        # issue the request  
        response = requests.get(url, params=dataValues, timeout=2)
        
        response.raise_for_status()   # cls

        # print out the response
        print(f"response status: { response.status_code } \n")
        if (response.status_code == 200):
            printResults(response)
    except HTTPError as err:
        print("Error: {0}".format(err))
    except Timeout as err:
        print("Request timeout {0}".format(err))

def printResults(resData):
    print(f"Response code: {resData.status_code} \n")

    print("Headers ----------------------------")
    print(resData.headers)
    print("\n")

    print("Returned data ------------------------")
    # print(resData.content)
    print(resData.text)

if __name__ == "__main__":
    main()