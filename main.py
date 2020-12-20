import tkinter as tk


# Set-up the window
window = tk.Tk()
window.title("Account Storage")



#Email entry frame
frm_emailEntry = tk.Frame(master=window)
ent_email_loc = tk.Entry(master=frm_emailEntry, width=20)
lbl_email = tk.Label(master=frm_emailEntry, text ="Email here")


#Password entry frame
frm_passwordEntry = tk.Frame(master=window)
ent_password_loc = tk.Entry(master=frm_passwordEntry, width=20)
lbl_password = tk.Label(master=frm_passwordEntry, text ="Password here")


#Hint entry frame
frm_hintEntry = tk.Frame(master=window)
ent_hint_loc = tk.Entry(master=frm_hintEntry, width=20)
lbl_hint = tk.Label(master=frm_hintEntry, text = "Hint here")


#layout of email entry and lab in frm_entry
#using the .grid() geometry manager
#email
ent_email_loc.grid(row=0, column=0, sticky='e')
lbl_email.grid(row=0, column=1, sticky='w')

#password
ent_password_loc.grid(row=1, column=0, sticky='e')
lbl_password.grid(row=1, column=1, sticky='w')

#hint
ent_hint_loc.grid(row=2, column=0, sticky='e')
lbl_hint.grid(row=2, column=1, sticky='w')


#definitons
def store_email():
    print(ent_email_loc.get())
    print(ent_password_loc.get())
    print(ent_hint_loc.get())


#Store email and password button
btn_emailbutton = tk.Button(
    master=window,
    text="Store!",
    command=store_email,
    )



#setup the layout using .grid() geometry manager
#email
frm_emailEntry.grid(row=0, column=0, pady=20)
btn_emailbutton.grid(row=4, column=1, pady=10)

#password
frm_passwordEntry.grid(row=1, column=0, pady=20)

#hint
frm_hintEntry.grid(row=2, column=0, pady=20)







window.mainloop()
