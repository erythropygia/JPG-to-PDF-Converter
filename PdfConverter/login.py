from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
from converter import *
from database import *
import os
import time


def login():
    
    mail=id_box.get()
    password=psw_box.get()
    if(mail=="" or password ==""):
        messagebox.showinfo("Pdf Converter","Mail veya Şifre Alanı Boş Bırakılamaz")
    else:
        if(login_database(mail,password)==1):
            root.destroy()
            os.system('main.py')
        else:
           messagebox.showinfo("Pdf Converter","Kullanıcı Adı ya da Şifre Hatalı") 
        

def sign_up():
    root.destroy()
    os.system('sign_up.py')
    

#Ana Pencerenin Tanımlanması
root=Tk()
root.title('PDF Converter')
root.geometry('300x300')

#Ekran Framelere Bölünüyor
frame_top=Frame(root,bg='#d3d3d3')
frame_top.place(relx=0.1, rely=0.27, relwidth=0.8, relheight=0.4)

#Login Butonu
select_button=Button(frame_top, text="Login", command=login)
select_button.place(relx=0.77,rely=0.22)

#Kayıt Ol Butonu
select_button=Button(frame_top, text="Sign Up", command=sign_up)
select_button.place(relx=0.75,rely=0.52)


#id textfield'i
id_box=Entry(frame_top)
id_box.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.2)
#id label
id_label=Label(frame_top,bg='#d3d3d3', text='   E-Mail:',font="Verdana 8 bold")
id_label.place(relx=0.0, rely=0.22)

#password textfield'i
psw_box=Entry(frame_top,show="*")
psw_box.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.2)
#password label
id_label=Label(frame_top,bg='#d3d3d3', text='Password:',font="Verdana 8 bold")
id_label.place(relx=0.0, rely=0.52)


root.mainloop()