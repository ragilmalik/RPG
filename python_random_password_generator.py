import secrets
import string
import os


def new_line():
    print("\n")

new_line()
# Defining how long should the generated password be
# 25 is usually the maximum allowed in most website
password_length = int()
while password_length < 10 or password_length > 25 :
    password_length = int(input("How long would you like the password to be? : "))
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
        
        import tkinter 
        import sys
        
        window = tkinter.Tk()  
        window.title("Your punishment")
        window.geometry("300x50")

        def func():
            with open("nggyu.txt", "r") as f:
                i = f.read()
                print(i)
         
        btn = tkinter.Button(window, text="Click here", command=func) 
        btn.pack() 

        window.mainloop()
        
        print("""now please get serious and enter any number between 10 and 25.
        No more messing around. Okay?""")
        new_line()

# TODO = catch exception if user enters other than integer or even empty in input


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







