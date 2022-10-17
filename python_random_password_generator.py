import secrets
import string
import os
from time import sleep
import webbrowser
import sys


with open("nggyu.txt", "r") as f:
    i = f.read()

def new_line():
    print("\n")

count = 0
count_word = 0

bye = False

new_line()
# Defining how long should the generated password be
# 25 is usually the maximum allowed in most website
password_length = int()
while password_length < 10 or password_length > 25 :
    password_length = input("How long would you like the password to be? : ")
    try :
        password_length = int(password_length)
        if password_length == 0 :
            print("I asked you how many characters you want, not how many friends you have...")
            new_line()
        elif password_length > 0 and password_length < 10:
            print("Minimum allowed is 10")
            new_line()
        elif password_length > 25 and password_length <= 100:
            print("Maximum allowed is 25")
            new_line()
        elif password_length > 100 or password_length < 0 :
            count +=1
            if count > 4 :
                print("You know what, i'm done with you.")
                sleep(3)
                link = "https://shoutsfromtheabyss.files.wordpress.com/2013/06/bye-homer.jpg"
                webbrowser.open(link)
                sleep(1)
                bye = True
                exit()

            if count > 3 :
                print("Well, you asked for this...")
                sleep(3)
                link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                webbrowser.open(link)
                sleep(1)
                new_line()
                print("Now please get serious and enter any number between 10 and 25. \nNo more messing around. Okay?")
                new_line()

            elif count > 2 :
                print("Oh you gotta be kidding me!")
                new_line()

            elif count > 1 :
                print("I am warning you...")
                new_line()

            else :
                print("Plese enter any number between 10 and 25.")
                new_line()
            

    except :
        if bye == True:
            exit()
        else :
            count_word +=1
            if count_word > 3 :
                link = "https://media.makeameme.org/created/fuck-you-hoe-353f50e1de.jpg"
                webbrowser.open(link)
                sleep(1)
                exit()
            elif count_word > 3 :
                print("LEAVE ME ALONEEEEEEEEE")
                password_length = int()
                new_line()
            elif count_word > 2 :
                print("oh...FUCK OFF!")
                password_length = int()
                new_line()
            elif count_word > 1 :
                print("Why is it so hard for you ? \nENTER A NUMBER! \nN-U-M-B-E-R")
                password_length = int()
                new_line()
            else :
                print("PLEASE ENTER A NUMBER")
                password_length = int()
                new_line()
                



big_letters = string.ascii_uppercase
low_letters = string.ascii_lowercase
digits = string.digits
special_characters = string.punctuation

new_line()
platform = input("Write the name of the application\
/website that you are going to use this password for? : ")

alphabet = big_letters + low_letters + digits + special_characters


while True: 
    password = ""
    for i in range(password_length):
        password += "".join(secrets.choice(alphabet))
    
    if ((any(char in special_characters for char in password) and 
        sum(char in digits for char in password) >= 2) and 
    (sum(char in big_letters for char in password) >= 1 and 
        sum(char in low_letters for char in password) >= 1)):
        break



with open("generated_password.txt", "a") as f:
    f.write(f"\nPassword for my {platform} : {password}")

directory = os.getcwd()

new_line()
print(f"Password for your {platform} : {password}")

new_line()
print(f"""You can go to :
    {directory}/generated_password.txt
    \t to see all of your generated passwords!""")




