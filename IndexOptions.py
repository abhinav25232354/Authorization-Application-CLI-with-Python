from libraries import *

def IndexOptionsShow():
    try:
        option = inquirer.select(
            # Choices for user Interaction
            message="Choose an option:",
            choices=[   
                    "Show Password",
                    "Critical Section",
                    "Personal Information", 
                    "Applications Log", 
                    "Exit"
                ],
            height=5
        ).execute()
        return option
    except Exception as e:
        print(e)
