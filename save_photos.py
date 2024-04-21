import urllib3

http = urllib3.PoolManager()

urls = [
	
]

for u in urls:
	url = u
	req = http.request('GET', url)
	print(u[u.rindex('/') + 1:])
	with open(u[u.rindex('/') + 1:], 'wb') as f:
		f.write(req.data)