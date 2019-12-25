import requests
import hashlib
import sys

# https://passwordsgenerator.net/sha1-hash-generator/
# url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
# res = requests.get(url)
# print(res)


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        # print(h, count)
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # print(password.encode('utf-8'))
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first5_char)
    count = get_password_leaks_count(response, tail)
    return count

    # return sha1_password


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f'{password} was found {count} times... you should change your password')
        else:
            print(f'{password} was NOT found. Carry on!')
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
