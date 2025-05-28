from libraries import *

def userAuthentication():
    """Authenticate User"""
    try:
        key = b'vTNkEGu1UpzKnYk8zZNV3UIRa8czF1gaYyxIQ03dFv0='
        cipher = Fernet(key)
        print("Authentication Service by Dexteritycoder")
        password = input("Enter Password: ")

        with open("confidential.txt", "rb") as f:
            pswd = bytes(f.read())
            decrypted_message = cipher.decrypt(pswd).decode()

        if decrypted_message == password:
            print("User Indentified! Welcome")
        else:
            print("User Not Identified!")
            a = input()
            exit()
    except Exception as e:
        print(e)