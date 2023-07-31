import requests
import hashlib
import sys

def requests_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}')
    return res
def passwordLeaksNum(hashes, tail):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if tail == h:
            return count
    return 0
def pwned_api(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    start, tail = sha1password[:5], sha1password[5:]
    response = requests_api_data(start)
    return passwordLeaksNum(response, tail)
def cmdcall():
    x = sys.argv[1:]
    for password in x:
        print(f'Password {password} has been leaked: {pwned_api(password)} times')

if __name__ ==  '__main__':
    cmdcall()
