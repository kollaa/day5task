
import requests as req

resp = req.get("https://github.com/sanspace/python-training/blob/main/day5/tasks.md")
html =resp.text
firsttitle = html.find("<title>")
start_index = firsttitle + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
print (title)