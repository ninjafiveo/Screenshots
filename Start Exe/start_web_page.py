# import os
# os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

from dataclasses import dataclass
import urllib.request

web_url = urllib.request.urlopen("https://google.com")
print("result code: "+str(web_url.getcode()))

data = web_url.read()
print(data)

# https://www.guru99.com/accessing-internet-data-with-python.html