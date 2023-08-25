# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


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

    if website == "" or passwordOutput == "":
        messagebox.showinfo(title="Ooops!🤦‍♀️", message="You have to fill all fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {emailOuput}"
                                                              f"\nPassword: {passwordOutput} \nIs it Ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {emailOuput} | {passwordOutput}\n")
                webInput.delete(0, END)
                passwordInput.delete(0, END)

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

webInput = Entry(width=35)
webInput.grid(row=1, column=1, columnspan=2)
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

gen_password = Button(text="Generate Password", command=generate_password)
gen_password.grid(row=3, column=2, columnspan=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()