import tkinter as tk
from tkinter import messagebox
import tkinter.messagebox

#variables

i= 7    #integer creates a new line on row 7++
a= 0    #a = email
b= 0    #b = password
c= 0    #c = hint
params = [a,b,c]  #makes params a variable that includes a, b and c

# Set-up the window
window = tk.Tk()
window.title("Account Storage")

#title lbl frame
frm_titlelbl = tk.Frame(master=window)
lbl_title = tk.Label(master=frm_titlelbl, text ="Account Storage")

#Email entry frame
frm_emailEntry = tk.Frame(master=window)
ent_email_loc = tk.Entry(master=frm_emailEntry, width=20)
lbl_email = tk.Label(master=frm_emailEntry, text ="Email: ")


#Password entry frame
frm_passwordEntry = tk.Frame(master=window)
ent_password_loc = tk.Entry(master=frm_passwordEntry, width=20)
lbl_password = tk.Label(master=frm_passwordEntry, text ="Password: ")


#Hint entry frame
frm_hintEntry = tk.Frame(master=window)
ent_hint_loc = tk.Entry(master=frm_hintEntry, width=20)
lbl_hint = tk.Label(master=frm_hintEntry, text = "Hint: ")


       
       #Functions

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
    print(a)
    print(b)
    print(c)
    f = open('Textdata.txt', 'a')
    f.write('Username: ' + a + ' ' + 'Password: ' + b + ' ' + 'Hint: ' + c + '\n')
    f.close()
    messagebox.showinfo('Added Entity', 'Successfully Added, \n' + 'Email: ' + a + '\nPassword: ' + b + '\nHint: ' + c + '\n')
    global i
    i= i + 1
   
 #opens file to grab any passwords and emails and stores them in row7 and above
def openfile():
    f = open("Textdata.txt", "r")
    frm_test = tk.Frame(master=window)
    test_test = tk.Label(master=frm_test, text =f.read())
    frm_test.grid(row=7)
    test_test.grid(row=7)
    f.close()
    test_test.grid_forget
    
            

       #BUTTONS
#Store email and password button
btn_emailbutton = tk.Button(master=window, text="Store!", command=store_file,)
btn_viewStorage = tk.Button(master=window, text="View", command= openfile,)
 
       
       
       
       
       #GRAPHICS
   
#layout of email entry and lab in frm_entry
#using the .grid() geometry manager

#title
frm_titlelbl.grid(row=0, columnspan=3)
lbl_title.grid(row=0, columnspan=3)
#email
ent_email_loc.grid(columnspan=3, row=1, column=1, sticky='W')
lbl_email.grid(row=1, sticky='E', padx=3)

#password
ent_password_loc.grid(columnspan=3, row=2, column=1, sticky='w')
lbl_password.grid(row=2, sticky='E', padx=3)

#hint
ent_hint_loc.grid(columnspan=3, row=3, column=1, sticky='w')
lbl_hint.grid(row=3, sticky='E', padx=3)

#setup the layout using .grid() geometry manager
#email
frm_emailEntry.grid(row=1, columnspan=2, pady=20)
btn_emailbutton.grid(row=4, column=1, pady=20)
btn_viewStorage.grid(row=4, column=2, pady=20)
#password
frm_passwordEntry.grid(row=2, columnspan=2, pady=20)

#hint
frm_hintEntry.grid(row=3, columnspan=2, pady=20)







window.mainloop()
