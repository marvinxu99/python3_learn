import requests
from requests.auth import HTTPBasicAuth

def main():

    # Access a URL that requires authentication - the format of
    # this URL is that you provide the username/password to auth against.
    url = "http://httpbin.org/basic-auth/MarvinXu/mySecret"

    # Create a credentials object using HTTPBasicAuth
    myCreds = HTTPBasicAuth("MarvinXu", "mySecret")

    # Issue the request with authentication credentials  
    response = requests.get(url, auth=myCreds)
    # ***You can also use a tuple for the (username, password)***
    # response = requests.get(url, auth=("MarvinXu", "mySecret"))

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