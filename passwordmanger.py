from cryptography.fernet import Fernet   # this module allows you to encrypt the texts

def load_key():
      file = open("key.key", "rb")
      key = file.read()
      file.close()
      return key


key = load_key() 
fer = Fernet(key)


'''def write_key():
      key = Fernet.generate_key()
      with open ("key.key","wb") as key_file:
           key_file.write(key)
'''


def view():
   with open('passwords.txt',"r") as f:
       for line in f.readlines():
            data = line.rstrip()
            user,pswd = data.split("|")
            print("User: ",user + " Password :",(fer.decrypt(pswd.encode()).decode()))

def add():
    name = input("Account name :")
    pwd = input ("Password : ")

    with open('passwords.txt',"a") as f:
       f.write(name + " | " + (fer.encrypt(pwd.encode()).decode())+ " \n")

while True :
     mode = input("would you like to add a new password or add an existing one (view,add) press q to quit  ?")
     if mode == "q":
          break
     
     if mode == "view":
          view()
     elif mode == "add":
          add()
     else:
          print("Invalid")
          continue