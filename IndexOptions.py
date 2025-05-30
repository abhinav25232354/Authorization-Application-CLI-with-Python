from libraries import *

def IndexOptionsShow():
    try:
        option = inquirer.select(
            # Choices for user Interaction
            message="\nChoose an option:",
            choices=[   
                    "Show Password",
                    "Add New Password",
                    "Delete a Entry",
                    "Critical Section",
                    "Personal Information", 
                    "Applications Log", 
                    "Exit"
                ],
            height=7
        ).execute()
        return option
    except Exception as e:
        print(e)
