# Usage: fuzzer.py /path/to/urllist.txt /robots.txt
# The above command would request any url in urllist.txt, let's say google.com, like this: https://google.com/robots.txt
# The fuzzer will output all requests that return 200s
import sys, socket, requests
 
host = sys.argv[1] # fuzzer.py (file path)
dir = sys.argv[2] # fuzzer.py (file path) (directory/file)
proto = sys.argv[3] # fuzzer.py (file path) (directory/file) http/https
lines = open(host).read().split('\n') # makes list with each domain from txt file
numURLS = len(lines)
pick = 0
if proto == "https" or proto == "":
	while pick < numURLS - 1:	
		response = requests.get("https://" + lines[pick] + dir)
		if response.status_code == 200:
			print("https://" + lines[pick] + dir) 
		pick = pick + 1	
elif proto == "http":
	while pick < numURLS - 1:	
		response = requests.get("http://" + lines[pick] + dir)
		if response.status_code == 200:
			print("http://" + lines[pick] + dir) 
		pick = pick + 1		

