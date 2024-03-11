from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #



def add_text_button():
    website_get = web_entry.get()
    email_get = email_entry.get()
    password_get = pass_entry.get()

    new_data = {
        website_get:{
            "email":email_get,
            "password":password_get
        }
    }

    if len(website_get) == 0 or len(password_get) == 0:
        messagebox.showinfo(title="Oops",message="Please Make Sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:

                data = json.load(data_file)
        except FileNotFoundError:

            with open("data.json", "w") as data_file:

                json.dump(new_data, data_file, indent=4)
        else:

            data.update(new_data)

            with open("data.json", "w") as data_file:

                json.dump(data,data_file, indent=4)
        finally:

            web_entry.delete(0, END)
            pass_entry.delete(0, END)

def find_password():
    website = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data file Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No Details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

Web = Label(text="Website:")
Web.grid(row=1,column=0)

Email = Label(text="Email/Username:")
Email.grid(row=2, column=0)

Pass = Label(text="Password:")
Pass.grid(row=3, column=0)

web_entry = Entry(width=18)
web_entry.grid(row=1, column=1)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "username@gmail.com")

pass_entry = Entry(width=18)
pass_entry.grid(row=3,column=1)

search_button = Button(text="Search",width=13, command=find_password)
search_button.grid(row=1, column=2)

Gen_pass = Button(text="Generate Password", command=generate_password)
Gen_pass.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add_text_button)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()