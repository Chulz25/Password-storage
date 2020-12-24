import tkinter as tk
from tkinter import messagebox
import tkinter.messagebox



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




#definitons

#stores email then prints in commandline
def store_email():
    print(ent_email_loc.get())
    print(ent_password_loc.get())
    print(ent_hint_loc.get())
    
 #opens file textdata.txt then prints input onto file
def store_file():
    a = ent_email_loc.get()
    b = ent_password_loc.get()
    c = ent_hint_loc.get()
    global params
    params = [a,b,c]
    print(a)
    print(b)
    print(c)
    f = open('Textdata.txt', 'a')
    f.write('Username: ' + a + '\n' + 'Password: ' + b + '\n' + 'Hint: ' + c + '\n')
    f.close()
    messagebox.showinfo('Added Entity', 'Successfully Added, \n' + 'Email: ' + a + '\nPassword: ' + b + '\nHint: ' + c + '\n')
    frm_email2 = tk.Frame(master=window)
    email_label2 = tk.Label(master=frm_email2, text = a )
    frm_email2.grid(row=7)
    email_label2.grid(row=7)

    frm_password2 = tk.Frame(master=window)
    password_label2 = tk.Label(master=frm_password2, text = b )
    frm_password2.grid(row=7, column=1)
    password_label2.grid(row=7, column=1)

    frm_hint2 = tk.Frame(master=window)
    hint_label2 = tk.Label(master=frm_hint2, text = c )
    frm_hint2.grid(row=7, column=2)
    hint_label2.grid(row=7, column=2)


#Store email and password button
btn_emailbutton = tk.Button(master=window, text="Store!", command=store_file,)

    #GRAPHICS
   
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

#setup the layout using .grid() geometry manager
#email
frm_emailEntry.grid(row=0, column=0, pady=20)
btn_emailbutton.grid(row=3, column=1, pady=20)

#password
frm_passwordEntry.grid(row=1, column=0, pady=20)

#hint
frm_hintEntry.grid(row=2, column=0, pady=20)






window.mainloop()
