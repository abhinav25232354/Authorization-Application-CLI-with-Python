from libraries import *

def showPassword():
    """Show Decrypted Password"""
    try:
        key = b'vTNkEGu1UpzKnYk8zZNV3UIRa8czF1gaYyxIQ03dFv0='
        cipher = Fernet(key)
        try:
            password = input("Enter Autentication (Password): ")
            with open("confidential.txt", "rb") as f:
                pswd = bytes(f.read())
                # encryptd_message = cipher.encrypt(pswd.encode())
                decrypted_message = cipher.decrypt(pswd).decode()
                # print(decrypted_message)
            
            if password == decrypted_message:
                print("Decrypted: ")
                print(decrypted_message)
            else:
                print("Invalid Credential")
        except Exception as e:
            print(f"Error: {e}")
    except Exception as e:
        print(e)