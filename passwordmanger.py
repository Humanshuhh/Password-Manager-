from cryptography.fernet import Fernet  # this module allows you to encrypt the texts
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import os



master_password= input("Enter your master password :")

def derive_key(master_password :str,salt :bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),   # hashing algorithm
        length=32,                   # 32 bytes = 256-bit key
        salt=salt,
        iterations=480000,           # makes brute-force very slow
        backend=default_backend()
    )

    #
    return base64.urlsafe_b64encode(kdf.derive(master_password.encode()))

def write_key(master_password: str):
    salt = os.urandom(16)      # 16 bytes
    derived_key = derive_key(master_password,salt)

    fernet_key = Fernet.generate_key()

    f = Fernet(derived_key)
    encrypted_fernet_key = f.encrypt(fernet_key)

    with open("key.key","wb") as key_file:
        key_file.write(salt + encrypted_fernet_key)
    print("Key generated and protected successfully !")

if not os.path.exists("key.key"):
    print("First time setup — generating your key...")

    write_key(master_password)
    print("Key created! Don't forget your master password.")
else:
    print("Key found — loading...")

def load_key(master_password : str):
    with open("key.key","rb") as key_file:
        data = key_file.read()
      
    salt = data[:16]
    encrypted_fernet_key = data[16:]

    derived_key = derive_key(master_password,salt)
    
    f = Fernet(derived_key)
    try:
        fernet_key = f.decrypt(encrypted_fernet_key)  # dercrypts the fernet key
        return fernet_key
    except Exception:
        print("Wrong password !")    # decrption fails if password is wrong
        exit()
    

key = load_key(master_password) 
fer = Fernet(key)

def view():
   try :
     with open('passwords.txt',"r") as f:
          lines = f.readlines()
          if not lines:
              print("No lines save yet")
              return
          for line in lines:
               data = line.rstrip()
               if not data:
                   continue
               user,pswd = data.split("|")
               print("User: ",user + " Password :",(fer.decrypt(pswd.encode()).decode()))
   except FileNotFoundError:
       print("No password file found")

def add():
    name = input("Account name :")
    pwd = input ("Password : ")

    with open('passwords.txt',"a") as f:
       f.write(name + " | " + (fer.encrypt(pwd.encode()).decode())+ " \n")
    print("Password saved")

def find():
    userid = input("Enter your user name")

    with open('passwords.txt',"r") as f:
        lines = f.readlines()
        found = False             # used a flag
        for line in lines:
               data = line.rstrip()
               if not data:
                   continue
               user,pswd = data.split("|")
               user = user.strip()
               pwd = user.strip()
               if(user == userid.strip()):
                    
                    print("User: ",userid + " Password :",(fer.decrypt(pswd.encode()).decode()))
                    found = True;
                    break
               
        if found == False:
            print("User name not found")

              

    
while True :
     mode = input("would you like to add a new password or add an existing one (view,add) press q to quit  ?")
     if mode == "q":
          break
     
     if mode == "view":
          view()
     elif mode == "add":
          add()
     elif mode == "find":
            find()
     else:
          print("Invalid")
          continue
