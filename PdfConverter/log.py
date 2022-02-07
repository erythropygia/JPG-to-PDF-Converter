# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 13:18:19 2021

@author: erythropygia
"""
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from turtle import back
from converter import *
from database import *
import time

#Ana Pencerenin Tanımlanması
root=Tk()
root.title('PDF Converter')
root.geometry('400x400')


#Fonksiyonlar
#Daha Önce Kullanılmış PDF'ler ve Kullanıcı Bilgileri

def list_print():
    log_data=open("LOG.txt","r")
    current_user=log_data.read()
    log_data.close()
    liste=list_pdf(current_user)
    if(liste):
        for i in liste:
            list_box.insert(END,i[1])
    else:
        list_box.insert(END,"NO PDF DATA IN DATABASE")
        
    
    uyelik_turu=account_type(current_user)
    uyelik_tarihi=premium_date(current_user)



    info_label.config(text='Your ID: '+current_user,font="Verdana 6 bold")
    info_label_2.config(text='Account Type',font="Verdana 7 bold")

    if(list_box.get(0)=="NO PDF DATA IN DATABASE"):
        info_label_1.config(text='Saved PDFs: 0',font="Verdana 6 bold")
    else:
        info_label_1.config(text='Saved PDFs: '+str(list_box.size()),font="Verdana 6 bold")
     
    if(uyelik_turu=='Premium'):
        info_label_3.config(text="Premium",font="Verdana 7 bold")
        info_label_4.config(text='',font="Verdana 7 bold")
    else:
        info_label_3.config(text='',font="Verdana 7 bold")
        info_label_4.config(bg='VioletRed3', text='No Premium',font="Verdana 7 bold")

#Üyelik Tarihi Kontrolü
    
    if(uyelik_tarihi==0):
        info_label_6.config(bg='#d3d3d3',text='Pre Date: NO PRE!', font="Verdana 5 bold")
        info_label_5.config(bg='#d3d3d3', text='EXP Date: NO PRE! ',font="Verdana 5 bold") 
        info_label_7.config(bg='#d3d3d3', text='Days: NO PRE! ',font="Verdana 5 bold")      
    else:
        info_label_6.config(bg='#d3d3d3',text='Pre Date: '+uyelik_tarihi[0], font="Verdana 5 bold")
        info_label_5.config(bg='#d3d3d3', text='EXP Date: '+uyelik_tarihi[1],font="Verdana 5 bold")
        info_label_7.config(bg='#d3d3d3', text='Days: '+str(uyelik_tarihi[2]),font="Verdana 5 bold")


#PDF'İ AÇMA FONKSİYONU
def openPdf():
    log_data=open("LOG.txt","r")
    current_user=log_data.read()
    log_data.close()
    liste=list_pdf(current_user)
    selected=list_box.curselection()
    ReConvert(current_user,list_box.get(selected))

#ÜYELİĞİ SİLME FONKSİYONU
def delete_Account():
    log_data=open("LOG.txt","r")
    current_user=log_data.read()
    log_data.close()
    control=messagebox.askyesno('Account Delete', 'Your account will be deleted, do you want to continue?')
    if(control==True):
        trigger(current_user)
        root.destroy()
        os.system('login.py')
        
    else:
        pass

#Ana Menüye Dönme Fonksiyonu
def back_main():
    root.destroy()
    os.system('main.py')
    
        
           
#Ekran Framelere Bölünüyor
frame_top=Frame(root,bg='#d3d3d3')
frame_top.place(relx=0.12, rely=0.05, relwidth=0.75, relheight=0.2)

frame_left=Frame(root,bg='#d3d3d3')
frame_left.place(relx=0.12, rely=0.28, relwidth=0.23, relheight=0.5)

frame_right=Frame(root,bg='#d3d3d3')
frame_right.place(relx=0.365, rely=0.28, relwidth=0.505, relheight=0.5)

frame_bottom=Frame(root,bg='#d3d3d3')
frame_bottom.place(relx=0.12, rely=0.79, relwidth=0.747, relheight=0.09)


#Frameler'e Alanlar Ekleniyor
#Ana Yazı / frame_top
main_label=Label(frame_top,bg='#d3d3d3', text='PDF Converter',font="Verdana 15 bold")
main_label.pack(padx=50,pady=25)

#frame_left
#Durum Labeli
status_label=Label(frame_left,bg='#d3d3d3', text='User Info',font="Verdana 9 bold")
status_label.place(relx=0,rely=0)
draw_label=Label(frame_left,bg='#d3d3d3', text='--------------',font="Verdana 9 bold")
draw_label.place(relx=0,rely=0.075)
info_label=Label(frame_left,bg='#d3d3d3', text='Your ID:',font="Verdana 6 bold")
info_label.place(relx=0,rely=0.15)
info_label_1=Label(frame_left,bg='#d3d3d3', text='Saved PDFs:',font="Verdana 6 bold")
info_label_1.place(relx=0,rely=0.25)

info_label_5=Label(frame_left,bg='#d3d3d3', text='EXP Date: ',font="Verdana 5 bold")
info_label_5.place(relx=0,rely=0.45)

info_label_6=Label(frame_left,bg='#d3d3d3', text='Pre Date: ',font="Verdana 5 bold")
info_label_6.place(relx=0,rely=0.35)

info_label_7=Label(frame_left,bg='#d3d3d3', text='Days: ',font="Verdana 5 bold")
info_label_7.place(relx=0,rely=0.55)

info_label_2=Label(frame_left,bg='#d3d3d3', text='Account Type:',font="Verdana 6 bold")
info_label_2.place(relx=0.11,rely=0.7)
info_label_3=Label(frame_left,bg='VioletRed3', text='',font="Verdana 7 bold")
info_label_3.place(relx=0.22,rely=0.8)
info_label_4=Label(frame_left,bg='#d3d3d3', text='',font="Verdana 7 bold")
info_label_4.place(relx=0.14,rely=0.8)

#frame_right
#ListBox Label
listBox_label=Label(frame_right,bg='#d3d3d3', text='LOG DATA',font="Verdana 9 bold")
listBox_label.place(relx=0, rely=0)
#ListBox
list_box=Listbox(frame_right)
list_box.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)


#frame_bottom
browse_button=Button(frame_bottom, text=" Open ", command=openPdf)
browse_button.place(relx=0.83,rely=0.15,relwidth=0.15)
browse_button.config(state=NORMAL)
delete_button=Button(frame_bottom, text= "Delete My Account", command=delete_Account)
delete_button.place(relx=0.01,rely=0.15,relwidth=0.4)
delete_button.config(state=NORMAL)
back_button=Button(frame_bottom, text=" Back ", command=back_main)
back_button.place(relx=0.60,rely=0.15,relwidth=0.15)
back_button.config(state=NORMAL)

#MenuBar 
my_menu=Menu(root)
root.config(menu=my_menu)
file_menu= Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)
 

list_print()
root.mainloop()
