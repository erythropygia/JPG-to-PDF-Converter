from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from converter import *
from database import *
import time


def register():
    isim=name_box.get()
    e_mail=id_box.get()
    password=psw_box.get()
    kredi_karti=kredi_box.get()
    cvv=cvv_box.get()
    expd=exd_box.get()

    
    if(r.get()==0):
        normal_account_register(isim,e_mail,password,0)

    else:
        pass
        premium_account_register(isim,e_mail,password,kredi_karti,cvv,expd,1)

    root.destroy()
    os.system('login.py')

def back():
    root.destroy()
    os.system('login.py')
    


#FORM GÖRÜNTÜLERİ
def premium():
    kredi_label.place(relx=0.45, rely=0.2)
    kredi_box.place(relx=0.65, rely=0.19, relwidth=0.25, relheight=0.1)

    cvv_label.place(relx=0.45, rely=0.35)
    cvv_box.place(relx=0.65, rely=0.34, relwidth=0.25, relheight=0.1)

    exd_label.place(relx=0.45,rely=0.50)
    exd_box.place(relx=0.65,rely=0.49,relwidth=0.25, relheight=0.1)

    uyelik_suresi_label.place(relx=0.45, rely=0.65)
    uyelik_suresi_1.place(relx=0.65, rely=0.65, relwidth=0.25, relheight=0.1)

    
def no_premium():
    kredi_label.place_forget()
    kredi_box.place_forget()

    cvv_label.place_forget()
    cvv_box.place_forget()

    uyelik_suresi_label.place_forget()
    uyelik_suresi_1.place_forget()

    exd_label.place_forget()
    exd_box.place_forget()



#Ana Pencerenin Tanımlanması
root=Tk()
root.title('PDF Converter')
root.geometry('600x400')

    
#Ekran Framelere Bölünüyor
frame_top=Frame(root,bg='#d3d3d3')
frame_top.place(relx=0.12, rely=0.05, relwidth=0.75, relheight=0.2)

frame_left=Frame(root,bg='#d3d3d3')
frame_left.place(relx=0.12, rely=0.28, relwidth=0.75, relheight=0.53)

frame_bottom=Frame(root)
frame_bottom.place(relx=0.12, rely=0.81, relwidth=0.747, relheight=0.1)


#Frameler'e Alanlar Ekleniyor
#Ana Yazı / frame_top
main_label=Label(frame_top,bg='#d3d3d3', text='PDF Converter',font="Verdana 25 bold")
main_label.pack(padx=50,pady=10)

#frame_right
#ListBox Label
listBox_label=Label(frame_left,bg='#d3d3d3', text='Register Page',font="Verdana 9 bold")
listBox_label.place(relx=0, rely=0)
#KAYIT FORMU ELEMANLARI
#İsim Soyisim Label,TextBox
name_label=Label(frame_left,bg='#d3d3d3', text='Name:',font="Verdana 8 bold")
name_label.place(relx=0, rely=0.2)
name_box=Entry(frame_left)
name_box.place(relx=0.16, rely=0.20, relwidth=0.25, relheight=0.1)
#E-Mail Label,TextBox
id_label=Label(frame_left,bg='#d3d3d3', text='E-Mail:',font="Verdana 8 bold")
id_label.place(relx=0, rely=0.35)
id_box=Entry(frame_left)
id_box.place(relx=0.16, rely=0.35, relwidth=0.25, relheight=0.1)
#Password Label,TextBox
psw_label=Label(frame_left,bg='#d3d3d3', text='Password:',font="Verdana 8 bold")
psw_label.place(relx=0, rely=0.5)
psw_box=Entry(frame_left)
psw_box.place(relx=0.16, rely=0.5, relwidth=0.25, relheight=0.1)
#Premium Üyelik Label,RadioButton
r=IntVar()
r.set("")
no_premium=Radiobutton(frame_left,text="No Thanks :(", variable=r,value=0,command=no_premium)
no_premium.place(relx=0.16, rely=0.8)
premium=Radiobutton(frame_left,text="Use Premium!", variable=r,value=1,command=premium)
premium.place(relx=0.16, rely=0.65)


#PREMİUM_ELEMANLARI
#KrediKartı Label,TextBox
kredi_label=Label(frame_left,bg='#d3d3d3', text='Credit Card:',font="Verdana 8 bold")
kredi_box=Entry(frame_left)
kredi_label.place_forget()
kredi_box.place_forget()
#Cvv Label,TextBox
cvv_label=Label(frame_left,bg='#d3d3d3', text='CVV:',font="Verdana 8 bold")
cvv_box=Entry(frame_left)
cvv_label.place_forget()
cvv_box.place_forget()
#Son Kullanım Tarihi,TextBox
exd_label=Label(frame_left,bg='#d3d3d3', text='Exp Date:',font="Verdana 8 bold")
exd_box=Entry(frame_left)
exd_label.place_forget()
exd_box.place_forget()
#Üyelik Süresi Label,RadioButton
uyelik_suresi_label=Label(frame_left,bg='#d3d3d3', text='Subscribe:',font="Verdana 8 bold")
uyelik_suresi_1=Checkbutton(frame_left,text="1 Month",command="")
uyelik_suresi_1.select()
uyelik_suresi_1.config(state=DISABLED)
uyelik_suresi_label.place_forget()
uyelik_suresi_1.place_forget()


#frame_bottom
#Button
#Kayıt_ol Butonu
register_button=Button(frame_bottom, text="Register", command=register)
register_button.place(relx=0.87,rely=0.18,relwidth=0.13)
register_button.config(state=NORMAL)
back_button=Button(frame_bottom, text="Back", command=back)
back_button.place(relx=0.70,rely=0.18,relwidth=0.13)
back_button.config(state=NORMAL)


root.mainloop()
