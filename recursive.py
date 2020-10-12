import os
import fnmatch

for roots, dirs, files in os.walk("."):
    for file in  fnmatch.filter(files, "*.py"):
        print("file = %s", file)
print(files)

