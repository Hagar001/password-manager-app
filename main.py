# Import Modules
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    symbols_range = list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127))
    symbols_list = [chr(choice(symbols_range)) for _ in range(randint(2, 4))]
    lowercase_list = [chr(randint(97, 122)) for _ in range(randint(4, 5))]
    uppercase_list = [chr(randint(65, 90)) for _ in range(randint(4, 5))]
    numbers_list = [chr(randint(48, 57)) for _ in range(randint(2, 4))]

    password_list = symbols_list + lowercase_list + uppercase_list + numbers_list
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.delete(0, END) # if I wrote anything in the password field then clicked generate, it should delete it first, or if I clicked generate more than once.
    pass_entry.insert(0, password) # 0 means adding it at the very star, at the beginning
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_input = website_entry.get()
    email_input = email_entry.get()
    pass_input = pass_entry.get()

    if len(website_input) == 0 or len(email_input) == 0 or len(pass_input) == 0:
        messagebox.showinfo(title="Oops", message="Please, don't leave any fields empty.")
    elif len(pass_input) < 8:
        messagebox.showinfo(title="Oops", message="Password should have at least 8 characters.")
    else:
        ok_to_save = messagebox.askokcancel(title=website_input,
                                            message=f"Data entered:\nEmail: {email_input}\n"
                                            f"Password: {pass_input}\nDo you want to save?")
        if ok_to_save:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_input} : {email_input} : {pass_input}\n")

    website_entry.delete(0, END) # from 0 to the end, all the text in it. the first char in index 0 until the end.
    pass_entry.delete(0, END) # we can add any indices for the beginning and the end of characters to delete.
    website_entry.focus()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=70)



canvas = Canvas(width=200, height=200, highlightthickness=0)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)

# Website:
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=60)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus() # This will put the cursor on it.

# Email/Username:
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=60)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "hagar@gmail.com")

# Password:
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

pass_entry = Entry(width=42)
pass_entry.grid(column=1, row=3)

pass_button = Button(text="Generate Password", command=generate_password)
pass_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", command=save, width=51)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()