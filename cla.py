import sys


number = int(sys.argv[1])

for i in range(number):
        print("hello world")

print(f"Name of the script      : {sys.argv[0]=}")
print(f"Arguments of the script : {sys.argv[1:]=}")
