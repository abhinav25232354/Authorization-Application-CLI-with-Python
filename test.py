import inquirer
import os
import json

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
