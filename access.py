import urllib.request
from urllib import parse
resp  = urllib.request.urlopen('https://github.com/sanspace/python-training/blob/main/day5/tasks.md')

data = resp.read()
html = data.decode("utf-8")
firsttitle = html.find("<title>")
start_index = firsttitle + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
print (title)
