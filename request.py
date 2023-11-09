import requests
import sys 

if len(sys.argv) < 2 :
	print("error argv")
	sys.exit(1)

url = f"http://{sys.argv[1]}"

req = requests.get(url)
print(req)
print(req.text)



