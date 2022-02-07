# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 13:18:19 2021

@author: erythropygia
"""
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from converter import *
import time


#Ana Pencerenin Tanımlanması
root=Tk()
root.title('PDF Converter')
root.geometry('600x400')


#Fonksiyonlar
#dosya seçme fonksiyonu
def openFile():
    global selecteditems
    file = filedialog.askopenfilenames(parent=root, title='Dosya Seçimi',filetypes=(("JPG Files", "*.jpg"),("PNG Files","*.png")))
    selecteditems=root.splitlist(file)
    counter = len(selecteditems)
    for i in range(counter):
        list_box.insert(END,selecteditems[i])
    #Convert Butonu aktif ediliyor
    if(counter !=0):
        convert_button.config(state=NORMAL)

#pdf kayıt fonksiyonu
def convertFile():
    counter=len(selecteditems)
    img_list=[]
    for i in range(counter):
        img_list.append(selecteditems[i])
    convert_images(img_list,len(selecteditems))
    browse_button.config(state=NORMAL)
    status_label.config(text='Convert Succesfull',font="Verdana 6 bold")
    convert_button.config(state=DISABLED)
    browse_box.config(state=NORMAL)
    
#pdf dosya yolu fonksiyonu
def savePath():
    data_name=browse_box.get()+".pdf"
    data_path="\\"+browse_box.get()+".pdf"
    save_pdf(data_name,data_path)
    status_label.config(text='Save Successfull',font="Verdana 6 bold")
    browse_button.config(state=DISABLED)
    browse_box.config(state=DISABLED)
    list_box.delete(0,END)

        
#Ekran Framelere Bölünüyor
frame_top=Frame(root,bg='#d3d3d3')
frame_top.place(relx=0.12, rely=0.05, relwidth=0.75, relheight=0.2)

frame_left=Frame(root,bg='#d3d3d3')
frame_left.place(relx=0.12, rely=0.28, relwidth=0.23, relheight=0.5)

frame_right=Frame(root,bg='#d3d3d3')
frame_right.place(relx=0.365, rely=0.28, relwidth=0.505, relheight=0.5)

frame_bottom=Frame(root,bg='#d3d3d3')
frame_bottom.place(relx=0.12, rely=0.81, relwidth=0.747, relheight=0.1)


#Frameler'e Alanlar Ekleniyor
#Ana Yazı / frame_top
main_label=Label(frame_top,bg='#d3d3d3', text='PDF Converter',font="Verdana 25 bold")
main_label.pack(padx=50,pady=10)

#frame_left
#Choose File Butonu
select_button=Button(frame_left, text="Choose File", command=openFile)
select_button.place(relx=0.25,rely=0.3)
#Convert Butonu
convert_button=Button(frame_left, text="Convert", command=convertFile)
convert_button.place(relx=0.315,rely=0.6)
convert_button.config(state=DISABLED)
#Durum Labeli
status_label=Label(frame_left,bg='#d3d3d3', text='',font="Verdana 10 bold")
status_label.place(relx=0.22,rely=0.85)


#frame_right
#ListBox Label
listBox_label=Label(frame_right,bg='#d3d3d3', text='File Path',font="Verdana 9 bold")
listBox_label.place(relx=0, rely=0)
#ListBox
list_box=Listbox(frame_right)
list_box.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)


#frame_bottom
#ListBox Label
SavePath_label=Label(frame_bottom,bg='#d3d3d3', text='Name:',font="Verdana 9 bold")
SavePath_label.place(relx=0.015, rely=0.23)
#ListBox
browse_box=Entry(frame_bottom)
browse_box.place(relx=0.13, rely=0.25, relwidth=0.72, relheight=0.5)
browse_box.insert(END,"untitled")
browse_box.config(state=DISABLED)
#Button
#Choose File Butonu
browse_button=Button(frame_bottom, text="Save", command=savePath)
browse_button.place(relx=0.88,rely=0.18,relwidth=0.1)
browse_button.config(state=DISABLED)


#MenuBar 

def data_LOG():
    root.destroy()
    os.system('log.py')
    
my_menu=Menu(root)
root.config(menu=my_menu)
file_menu= Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Data LOG",command=data_LOG)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)
 


root.mainloop()
