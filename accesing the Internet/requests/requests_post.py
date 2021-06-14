import requests

def main():

    url = "http://httpbin.org/post"

    # some parameters to the URL via a GET request
    # Note that requests handles this for you, no manual encoding
    dataValues = {
        "key1": "value1",
        "key2": "value2"
    }

    # Pass a custom header to the server
    headerValues = {
        "User-Agent": "Marvin Xu App / 1.0.1",
    }

    # issue the request  
    response = requests.post(url, data=dataValues, headers=headerValues)

    # print out the response
    print(f"response status: { response.status_code }")
    if (response.status_code == 200):
        printResults(response)


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