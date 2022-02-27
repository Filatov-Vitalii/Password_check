#The password is "My password"

from tkinter import *
import time

def password_hide():

    def change_button_name():
        if show_hide_button["text"] == "Hide":
            show_hide_button["text"] = "Show"
        elif show_hide_button["text"] == "Show":
            show_hide_button["text"] = "Hide"

    def change_text_visibility():
        if entry["show"] == "":
            entry["show"] = "*"
        elif entry["show"] == "*":
            entry["show"] = ""

    change_button_name()
    change_text_visibility()

def entering_profile():
    label_2["text"] = "Entering your profile...\n(This operation may take forever)"
    entry["state"] = DISABLED
    show_hide_button["state"] = DISABLED
    submit_button["state"] = DISABLED

def submit():
    submited_password = entry.get()
    if submited_password == "My password":
        entering_profile()
    else:
        label_2["text"] = "Wrong password!"

password_window = Tk()

password_window.title("Enter your password")
password_window.geometry("600x150")

label_1 = Label(password_window, font=("Arial", 18), text="Please enter your password:")
label_1.pack()

entry = Entry(password_window, font=("Arial", 15), show="*", state=NORMAL)
entry.pack(side=LEFT)

show_hide_button = Button(password_window,
                          font=("Arial", 12),
                          text="Show",
                          command=password_hide,
                          state=ACTIVE)
show_hide_button.pack(side=LEFT)

submit_button = Button(password_window,
                       font=("Arial", 12),
                       text="Submit",
                       command=submit,
                       state=ACTIVE)
submit_button.pack(side=LEFT)

label_2 = Label(password_window, font=("Arial", 12, "bold"), text="", padx=20)
label_2.pack(side=LEFT)

password_window.mainloop()