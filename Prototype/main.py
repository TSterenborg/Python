import os

def signup():

    loginkey = input("Create key: ")

    file = open("./Prototype/key.txt", "a")

    file.write(loginkey)
    file.close()

    login()

def login():
    askkey = input("Key: ")

    with open("./Prototype/key.txt", "r") as file:
        key = {}
        for line in file:
            if line.strip() == askkey:
                start()
                return
    wrong = input("wrong key! want to reset? type \"resetkey\" ")
    if wrong == "resetkey":
        resetkey()

def resetkey():
    os.remove("./Prototype/key.txt")
    signup()

def start():
    result = input("Create or Request: ").lower()

    if result == "create":
        create()
    elif result == "request":
        if os.path.getsize("./Prototype/data.txt") == 0:
            print("File is empty")
        else:
            request()
    else:
        exit()

def create():
    site = input("Site: ").capitalize()
    username = input("Username: ")
    password = input("Password: ")

    data = [username, password]

    file = open("./Prototype/data.txt", "a")

    file.write(f"\n{site} {data}")
    file.close()

    print(f"{site} has been added to your saved accounts!")

    exit()

def request():
    request = input("What Site: ").capitalize()
    try:
        with open("./Prototype/data.txt", "r") as file:
            first_words = []
            next(file)
            for line in file:
                words = line.split()
                if words:
                    first_words.append(words[0])

        if request in first_words:
            with open("./Prototype/data.txt") as file:
                for line in file:
                    if request in line:
                        print(line.strip())
        else:
            notfound = input("Site not found, want to create the data? Type \"create\" ")
            if notfound == "create":
                create()
            else:
                exit()
    except StopIteration:
        print("File is empty")
        exit()


open("./Prototype/key.txt", "a")
open("./Prototype/data.txt", "a")

if os.path.getsize("./Prototype/key.txt") == 0:
    signup()
else:
    login()