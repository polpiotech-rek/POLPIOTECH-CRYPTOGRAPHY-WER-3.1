from termcolor import cprint, colored
from os import system, chdir
from time import sleep
import colorama, os, getpass

colorama.init
print()
print()
try:
    cprint("ENTER VALUE ENCRYPTION ALGORITHM:", "white", "on_red")
    algValue = int(getpass.getpass("ENTER VALUE: "))
    algKey = int(algValue)
    def decrypt(message, key=algKey):
        encrypted = ""
        for mark in message:
            codeASCII = ord(mark)
            codeASCII -= key
            while codeASCII > 126:
                codeASCII -= 95
            while codeASCII < 32:
                codeASCII +=95
            encrypted += chr(codeASCII)
        return encrypted
    print()
    cprint("DO YOU WANT SAVE THIS FILE? (y/n)", "white", "on_red") 
    saveFile = input("YOUR CHOICE: ")
    if saveFile == "y":
        print()
        print()
        cprint("INFORMATION:", "white", "on_red")
        cprint(" * [ D ] - COLOR YELLOW - DIRECTORY", "black", "on_white")
        cprint(" * [ F ] - COLOR BLUE - FILE       ", "black", "on_white")
        print()
        path = str(input('ENTER PATH: '))
        print()
        os.chdir(path)
        cprint("GO TO DIRECTORY:", "white", "on_red")
        path_directory_destination = os.getcwd()
        print(colored("[ SAVE PATH ]","black", "on_white"), colored(path, "black", "on_white"))
        for item in os.listdir('.'):
            if os.path.isdir(item):
                cprint('{} - [ D ]'.format(item), "white", "on_blue")
            else:
                cprint('{} - [ F ]'.format(item), "black", "on_yellow") 
        print()
        cprint("YOUR MESSAGE TO BE DECRYPTED:", "white", "on_red")
        text = str(input("ENTER TEXT FOR DECRYPTION: "))
        print()
        cprint("CONTENT DECRYPTED MESSAGE:", "white", "on_red")
        cprint(decrypt(text), 'yellow')
        print()
        encText = decrypt(text)
        cprint("SAVING THE ENCRYPTED TEXT TO A FILE:", "white", "on_red")
        file_name = str(input('ENTER A FILE NAME: '))
        print()
        f = open(file_name, "w", encoding="utf-8")
        with open(file_name, 'w') as f:
            f.write(encText)
        f.close()
    elif saveFile == "n":
        print()
        cprint("YOUR MESSAGE TO BE DECRYPTED:", "white", "on_red")
        text = str(input("ENTER TEXT FOR DECRYPTION: "))
        print()
        cprint("CONTENT DECRYPTED MESSAGE:", "white", "on_red")
        cprint(decrypt(text), 'yellow')
        print()
        encText = decrypt(text)
        print()
    else:
        print()
        cprint("AN INCORRECT OPTION HAS BEEN SELECTED!", "white", "on_red")
        print()
        print()
except ValueError:
    print()
    cprint("(ValueError): YOU MUST USE NUMBERS!", "white", "on_red")
    sleep(3)
    path_program = "/home/rekbod/Pulpit/Projects/Python/POLPIOTECH® CRYPTOGRAPHY/Modules/"
    chdir(path_program)
    system("python3 polpiotech-decryption.py")
except TypeError:
    print()
    cprint("(TypeError): YOU MUST USE NUMBERS!", "white", "on_red")
    sleep(3)
    path_program = "/home/rekbod/Pulpit/Projects/Python/POLPIOTECH® CRYPTOGRAPHY/Modules/"
    chdir(path_program)
    system("python3 polpiotech-decryption.py")
except FileNotFoundError:
    cprint("(FileNotFoundError): WRONG PATH ENTERED!", "white", "on_red")
    sleep(3)
    path_program = "/home/rekbod/Pulpit/Projects/Python/POLPIOTECH® CRYPTOGRAPHY/Modules/"
    chdir(path_program)
    system("python3 polpiotech-decryption.py")
except Exception as otherExcept:
    print()
    cprint(f"AN ERROR HAS OCCURED {otherExcept}!", "white", "on_red")
    sleep(3)
    path_program = "/home/rekbod/Pulpit/Projects/Python/POLPIOTECH® CRYPTOGRAPHY/Modules/"
    chdir(path_program)
    system("python3 polpiotech-decryption.py")