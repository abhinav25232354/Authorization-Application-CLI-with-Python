try:
    from libraries import * # All Libraries used in the Whole program is stored here
    from authentication import userAuthentication # Authentication of user based on Entered Password
    from PasswordRequest import showPassword # Shows Password only after authenticating user
    from IndexOptions import IndexOptionsShow # Shows Options at the exection of program for better user friendly Environment
    from activitymonitoring import generate_report # Generates summarized report of whole system from last boot
    from ForAuthorityOnly import criticalSection # Critical section stores passwords and other credentials safe from others
    from NewAppendence import AddNewPasscode # For Adding New Entry in Critical Section
    from NewAppendence import deleteEntry # For Deleting a existing entry by navigating through json
except Exception as e:
    print(e)

try:    
    init() # colorama initialization
    userAuthentication() 
except Exception as e:
    print(e)

try:
    def Exit(): print("Thanks for Using My Software"), exit()
    def personal_information(): print("Under Development")
except Exception as e:
    print(e)

try:
    while True:
        option = IndexOptionsShow()
        if option == "Show Password":
            showPassword() # Active
        elif option == "Add New Password":
            AddNewPasscode() # Active
        elif option == "Delete a Entry":
            deleteEntry() # Active
        elif option == "Critical Section":
            criticalSection() # Active
        elif option == "Personal Information":
            personal_information() # Not Active
        elif option == "Applications Log":
            print(generate_report()) # Active
        elif option == "Exit":
            Exit()
            break
        else:
            print(Fore.GREEN, option, Fore.RESET)
except Exception as e:
        print(e)