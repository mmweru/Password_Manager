# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for char in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)

    passwordInput.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- save PASSWORD ------------------------------- #
def save():
    website = webInput.get()
    emailOuput = emailInput.get()
    passwordOutput = passwordInput.get()
    new_data = {
        website : {
            "email": emailOuput,
            "password": passwordOutput
        }
    }

    if website == "" or passwordOutput == "":
        messagebox.showinfo(title="Ooops!🤦‍♀️", message="You have to fill all fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            webInput.delete(0, END)
            passwordInput.delete(0, END)


#_____________________________FIND PASSWORD __________________________#
def find_password():
    website = webInput.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

webpage = Label(text="Website:")
webpage.grid(row=1, column=0)

webInput = Entry(width=21)
webInput.grid(row=1, column=1)
webInput.focus()

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

emailInput = Entry(width=35)
emailInput.grid(row=2, column=1, columnspan=2)
emailInput.insert(0, "mwerumaryann@gmail.com")

password = Label(text="Password:")
password.grid(row=3, column=0)

passwordInput = Entry(width=21)
passwordInput.grid(row=3, column=1)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

gen_password = Button(text="Generate Password", command=generate_password)
gen_password.grid(row=3, column=2, columnspan=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()