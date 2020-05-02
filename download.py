import requests
import os
import time


url_list = []
if not os.path.exists("results"):
  os.mkdir("results")

with open('memo.txt') as f:
  for i in f:
     url_list.append(i.strip())


def save_image(url, name):
  res = requests.request("GET", url)
  content = res.content
  extension = url.split("/")[-1]
  filename = name + "." + extension
  with open("results/"+filename, 'wb') as f:
    f.write(content)  

for i, url in enumerate(url_list):
  time.sleep(1)
  save_image(url, str(i))
