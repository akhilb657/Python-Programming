import re
import urllib.request

sites = ["google.com"]

for s in sites:
    print("Searching ",s)
    response = urllib.request.urlopen("http://"+s)
    text = response.read()
    title = re.findall("<title>.*</title>",str(text),re.I)
    print(title)