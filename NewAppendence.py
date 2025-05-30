from libraries import *

try:
    key = b'vTNkEGu1UpzKnYk8zZNV3UIRa8czF1gaYyxIQ03dFv0='
    cipher = Fernet(key)
except Exception as e:
    print(e)

def load_json(filename):
    try:
        if not os.path.exists(filename):
            return {}
        with open(filename, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    except Exception as e:
        print(e)

def save_json(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(e)

def add_simple_key_value():
    try:
        key = input("Enter key: ")
        value = input("Enter value: ")
        return key, value
    except Exception as e:
        print(e)

def add_dict():
    try:
        print("Adding a dictionary...")
        sub_dict = {}
        while True:
            k = input("  Enter sub-key (or 'done' to finish): ")
            if k.lower() == 'done':
                break
            v = input(f"  Enter value for '{k}': ")
            sub_dict[k] = v
        return sub_dict
    except Exception as e:
        print(e)

def add_list_of_dicts():
    try:
        print("Adding a list of dictionaries...")
        list_of_dicts = []
        while True:
            print(f"  Creating dictionary #{len(list_of_dicts) + 1}")
            new_dict = add_dict()
            list_of_dicts.append(new_dict)
            again = input("  Add another dictionary to the list? (y/n): ").strip().lower()
            if again != 'y':
                break
        return list_of_dicts
    except Exception as e:
        print(e)

def merge_values(existing, new):
    try:
        if isinstance(existing, dict) and isinstance(new, dict):
            existing.update(new)
            return existing
        elif isinstance(existing, list):
            if isinstance(new, list):
                existing.extend(new)
            else:
                existing.append(new)
                return existing
        else:
            return [existing, new]  # Merge scalar into a list
    except Exception as e:
        print(e)

def AddNewPasscode():
    try:
        with open("confidential.txt", "rb") as f:
            pswd = bytes(f.read())
            decrypted_message = cipher.decrypt(pswd).decode()
            input_password = input("Enter Passcode: ")
            if decrypted_message == input_password:
                filename = "passwords.json"
                data = load_json(filename)

                main_key = input("Enter main key under which you want to store data: ")

                if main_key not in data:
                    data[main_key] = {}

                while True:
                    print("\nChoose a type of data to add:")
                    print("1. Simple key-value")
                    print("2. Dictionary as value")
                    print("3. List of dictionaries")
                    print("4. Exit and Save")

                    choice = input("Your choice (1/2/3/4): ").strip()

                    if choice == '1':
                        k, v = add_simple_key_value()
                        if k in data[main_key]:
                            print("⚠️  Key exists. Merging...")
                            data[main_key][k] = merge_values(data[main_key][k], v)
                        else:
                            data[main_key][k] = v

                    elif choice == '2':
                        k = input("Enter key to assign the dictionary to: ")
                        new_dict = add_dict()
                        if k in data[main_key]:
                            print("⚠️  Key exists. Merging dictionaries...")
                            data[main_key][k] = merge_values(data[main_key][k], new_dict)
                        else:
                            data[main_key][k] = new_dict

                    elif choice == '3':
                        k = input("Enter key to assign the list of dictionaries to: ")
                        new_list = add_list_of_dicts()
                        if k in data[main_key]:
                            print("⚠️  Key exists. Appending to existing list...")
                            data[main_key][k] = merge_values(data[main_key][k], new_list)
                        else:
                            data[main_key][k] = new_list

                    elif choice == '4':
                        break
                    else:
                        print("Invalid choice. Try again.")

                save_json(data, filename)
                print(f"\n✅ Data saved successfully to '{filename}'.")
            else:
                print("Invalid Credential")
                return
    except Exception as e:
        print(e)


def delete_entry():
    try:
        filename = "passwords.json"
        data = load_json(filename)

        if not data:
            print("No data to delete.")
            return

        path = []
        current = data

        while isinstance(current, dict) and current:
            choice = inquirer.select(
                message="Choose a key to explore or delete:",
                choices=list(current.keys()),
                height=10
            ).execute()

            path.append(choice)
            current = current[choice]

        # Confirm deletion
        full_path = " → ".join(path)
        confirm = inquirer.confirm(
            message=f"Do you really want to delete '{full_path}'?",
            default=False
        ).execute()

        if confirm:
            # Navigate and delete the key from parent
            target = data
            for key in path[:-1]:
                target = target[key]
            deleted_key = path[-1]
            del target[deleted_key]

            save_json(data, filename)
            print(f"🗑️  Deleted '{full_path}' successfully.")
        else:
            print("❌ Deletion cancelled.")

    except Exception as e:
        print(e)

# if __name__ == "__main__":
    # main()
