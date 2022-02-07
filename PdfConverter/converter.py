from PIL import Image
import os
from database import *



im_list=[]
im_list_check=[]

def convert_images(list_box,countselecteditem):
    global im_list
    global im_list_check
    
    for i in range(countselecteditem):
        im_list.append(Image.open(list_box[i]))
    
    for i in range (0,countselecteditem):
        im_list_check.append(im_list[i])
    

def save_pdf(data_name,data_path):
    global im_list_check
    image_1=im_list_check[0]
    im_list_check.remove(image_1)
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    pdf1_filename=desktop+data_path
    image_1.save(pdf1_filename, "PDF" , resolution=100.0, save_all=True, append_images=im_list_check)
    #Database Kayıt Fonksiyonu
    pdfsaveDatabase(data_name,pdf1_filename)