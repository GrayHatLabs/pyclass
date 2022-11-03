import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():

    if file == "ransomware.py" or file == "akey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("akey.key","rb") as thekey:
    secretkey = thekey.read()
    print(secretkey)
for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
        contents_decrytped = Fernet(secretkey).decrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_decrytped)
