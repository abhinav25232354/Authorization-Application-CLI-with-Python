from libraries import *

try:
    key = b'vTNkEGu1UpzKnYk8zZNV3UIRa8czF1gaYyxIQ03dFv0='
    cipher = Fernet(key)
except Exception as e:
    print(e)

def criticalSection():
    """Critical Section is only for authorised personnel"""
    try:
        def navigate_json(data):
            while isinstance(data, dict):
                choice = inquirer.select(
                    message="Choose a key:",
                    choices=list(data.keys()),
                    height=10
                ).execute()
                data = data[choice]
            return data

        # Load JSON file
        with open("passwords.json") as js:
            jFile = json.load(js)

        # Navigate and retrieve final value
        final_value = navigate_json(jFile)
        with open("confidential.txt", "rb") as f:
            pswd = bytes(f.read())
            decrypted_message = cipher.decrypt(pswd).decode()
        input_password = input("Enter Passcode: ")
        if decrypted_message == input_password:
            print(f"Credential: {final_value}")
        else:
            return
    except Exception as e:
        print(e)

# criticalSection()