# 🔐 Password Manager

A simple command-line Password Manager built with Python that allows users to securely store and retrieve passwords using Fernet encryption from the Cryptography library.

## 🚀 Features

* Add new account credentials
* Store passwords in encrypted format
* View saved passwords by decrypting them
* Simple and easy-to-use command-line interface
## How Your Password Manager Works — Step by Step

**1. Master password entry**
When the program starts, it asks you to type a **master password** — this never gets saved anywhere, it only exists in your head and in memory while the program runs.

**2. Key derivation (PBKDF2)**
Your master password is run through a **Key Derivation Function** along with a random **salt**, producing a strong 32-byte cryptographic key. This step is slow on purpose (480,000 iterations) to resist brute-force attacks.

**3. First run — key generation**
If `key.key` doesn't exist yet, the program generates a **random Fernet key** (the actual encryption key used for your passwords) and encrypts *that* key using the derived key from step 2. The salt + encrypted Fernet key are saved together into `key.key`.

**4. Every other run — key loading**
On subsequent runs, the program reads `key.key`, extracts the salt, re-derives the same key from your master password + salt, and uses it to **decrypt** the stored Fernet key. If you type the wrong master password, decryption fails and access is denied.

**5. Fernet object created**
Once the real Fernet key is recovered, a `Fernet(key)` object (`fer`) is created — this object is what actually encrypts/decrypts your individual account passwords.

**6. Adding a password**
When you choose "add," you enter an account name and password. The password is encrypted using `fer.encrypt()`, and the line `account_name|encrypted_password` is appended to `passwords.txt`.

**7. Viewing all passwords**
When you choose "view," the program reads every line in `passwords.txt`, splits each into `user` and `encrypted password`, decrypts the password with `fer.decrypt()`, and prints them.

**8. Finding a specific password**
When you choose "find," you enter a username; the program searches line-by-line through `passwords.txt`, and once it finds a matching account name, decrypts and displays just that one password.

**9. Why it's secure**
Passwords in the file are never stored in plain text — they're encrypted with the Fernet key. The Fernet key itself is never stored in plain text either — it's encrypted with a key derived from your master password. So two layers of protection exist, and without your master password, neither the Fernet key nor your saved passwords can be recovered.

## 🛠️ Technologies Used

* Python 3
* Cryptography (Fernet)

## 📂 Project Structure

```text
Password-Manager/
│
├── passwordmanager.py
├── passwords.txt
├── key.key
├── README.md
└── requirements.txt
```



## 📖 How It Works

1. The user chooses whether to add or view passwords.
2. Passwords are encrypted using Fernet encryption before being stored.
3. Encrypted passwords are saved in a text file.
4. Stored passwords can be decrypted and viewed when required.

## 🎯 Learning Outcomes

This project helped me understand:

* File Handling in Python
* Functions and Modular Programming
* Encryption and Decryption
* Working with External Libraries
* Command-Line Applications

## 🔮 Future Improvements

* Password Generator
* Password Strength Checker
* Search Functionality


## 👨‍💻 Author

Priyanshu

---

⭐ If you found this project useful, consider starring the repository.
