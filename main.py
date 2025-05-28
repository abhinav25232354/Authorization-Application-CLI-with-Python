from libraries import *
from authentication import userAuthentication
from PasswordRequest import showPassword
from IndexOptions import IndexOptionsShow
from activitymonitoring import system_activity_log

init() # colorama initialization
userAuthentication()
        
def critical_section(): pass
def personal_information(): pass
def application_log(): pass
def Exit(): pass


while True:
    option = IndexOptionsShow()
    if option == "Show Password":
        showPassword() # Active
    elif option == "Critical Section":
        critical_section()
    elif option == "Personal Information":
        personal_information()
    elif option == "Application Log":
        system_activity_log() # Active
    elif option == "Exit":
        Exit()
        break
    else:
        print(Fore.GREEN, option, Fore.RESET)