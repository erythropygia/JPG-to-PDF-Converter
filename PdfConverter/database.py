import mysql.connector
from mysql.connector import Error 
import base64
import os
from tkinter import messagebox
import datetime
import webbrowser



#KULLANICI GİRİŞİ FONKSİYONLARI
def login_database(mail,password_1):
    host="localhost"
    user="root"
    password="1234"
    database="pdf_converter"
     
    #Kullanıcı adı kontrol
    mydb=mysql.connector.connect(host=host,user=user,password=password,database=database)
    cursor=mydb.cursor()
    query="SELECT * from 1_kullanici_giris WHERE kullanici_mail=%s"
    cursor.execute(query,[(mail)])
    giris_kontrol=cursor.fetchone()
    if(giris_kontrol):
        for i in giris_kontrol:
            if(password_1==str(giris_kontrol[2])):
                log_data=open("LOG.txt","w+")
                log_data.write(str(get_kullanici_id(mail)))
                log_data.close()
                return 1
                break                  
    else:
        print("Giriş Başarısız")
        return 0    



#PDF KAYIT FONKSİYONLARI 
def convertToBinary(filename):
    with open(filename,'rb') as file:
        binarydata=file.read()
    return binarydata


def convertBinaryToFile(binarydata,filename):
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    with open(filename,'wb') as file:
        file.write(binarydata)


def pdfsaveDatabase(data_name,filename):
  
    host="localhost"
    user="root"
    password="1234"
    database="pdf_converter"

    log_data=open("LOG.txt","r")
    current_user=log_data.read()
    log_data.close()
     
    try:
        connection=mysql.connector.connect(host=host,user=user,password=password,database=database)
        cursor=connection.cursor()
        insertQuery=""" INSERT into pdfler(pdf_adi,kullanici_ID,pdf_data) value (%s,%s,%s)"""
        convert_pdf=convertToBinary(filename)
        value=(data_name,current_user,convert_pdf)
        cursor.execute(insertQuery,value)
        connection.commit()
        result=cursor.fetchmany(size=4)
    except Error as e:
        print("Error occured",e)
      
    finally:
        if(connection.is_connected()):
            print("Kayıt Tamamlandı")

#PDF ReCONVERT FONKSİYONU - DB'DEKİ BLOB DATAYI PDF E ÇEVİREN FONKSİYON

def ReConvert(current_user,pdf_name):
    print("User: "+ current_user + ", Pdf Name: " + pdf_name)

    host="localhost"
    user="root"
    password="1234"
    database="pdf_converter"
    #İstenen PDF'i Bulma
    mydb=mysql.connector.connect(host=host,user=user,password=password,database=database)
    cursor=mydb.cursor()
    query="SELECT pdf_data from pdfler WHERE kullanici_ID=%s AND pdf_adi=%s"
    cursor.execute(query,[(current_user),(pdf_name)])
    kontrol=cursor.fetchall()
    pdf_data=kontrol[0][0]
    convertBinaryToFile(pdf_data,pdf_name)
    webbrowser.open_new(pdf_name)
    



#DATABASE LİSTELEME FONKSİYONLARI
def list_pdf(kullanici_ID):
    host="localhost"
    user="root"
    password="1234"
    database="pdf_converter"
     
    #Kullanıcı adı kontrol
    mydb=mysql.connector.connect(host=host,user=user,password=password,database=database)
    cursor=mydb.cursor()
    query="SELECT pdf_ID,pdf_adi from pdfler WHERE kullanici_ID=%s"
    cursor.execute(query,[(kullanici_ID)])
    giris_kontrol=cursor.fetchall()
    if(giris_kontrol):
        for i in giris_kontrol:
            return giris_kontrol
    else:
        return 0    
    
def account_type(kullanici_ID):
    host="localhost"
    user="root"
    password="1234"
    database="pdf_converter"
    mydb=mysql.connector.connect(host=host,user=user,password=password,database=database)
    cursor=mydb.cursor()
    query="SELECT kullanici_uyelik_duzeyi from 2_bilgiler WHERE kullanici_ID=%s"
    cursor.execute(query,[(kullanici_ID)])
    giris_kontrol=cursor.fetchone()
    
    if(giris_kontrol[0]==1):
            return "Premium"
    else:
        return "No Premium"    
        
###### KAYIT FONKSİYONLARI ######

##### NORMAL REGISTER #####

def normal_account_register(isim,e_mail,password,uyelik_turu):
    host="localhost"
    user="root"
    password="1234"
    database="pdf_converter"
     
    try:
        connection=mysql.connector.connect(host=host,user=user,password=password,database=database)
        cursor=connection.cursor()
        #1_kullanici_giris kayıtları
        insertQuery="""INSERT into 1_kullanici_giris(kullanici_mail,kullanici_sifre) value (%s,%s)"""
        value=(e_mail,password)
        cursor.execute(insertQuery,value)
        connection.commit()
        result=cursor.fetchmany(size=4)
        #KULLANICI_ID'SİNİ ALMA
        kullanici_ID=get_kullanici_id(e_mail)
        bilgiler_kayit(kullanici_ID,isim,e_mail,uyelik_turu)

        
    except Error as e:
        print("Error occured",e)
      
    finally:
        if(connection.is_connected()):
            print("Kullanıcı Bilgiler Kaydı Tamamlandı")
           
            connection.close()
           

def get_kullanici_id(e_mail):
    host="localhost"
    user="root"
    password="1234"
    database="pdf_converter"
     
    #Kullanıcı adı kontrol
    mydb=mysql.connector.connect(host=host,user=user,password=password,database=database)
    cursor=mydb.cursor()
    cursor.execute("SELECT kullanici_ID from 1_kullanici_giris where kullanici_mail='"+e_mail+"'")
    kullanici_id=cursor.fetchone()
    mydb.close()
    return kullanici_id[0]

def bilgiler_kayit(kullanici_ID,isim,e_mail,uyelik_turu):
    #2_kullanici_bilgiler kayıtları
    host="localhost"
    user="root"
    password="1234"
    database="pdf_converter"
     
    try:
        connection=mysql.connector.connect(host=host,user=user,password=password,database=database)
        cursor=connection.cursor()
        #1_kullanici_giris kayıtları
        insertQuery="""INSERT into 2_bilgiler(kullanici_ID,kullanici_isim_soyisim,kullanici_mail,kullanici_uyelik_duzeyi) value (%s,%s,%s,%s)"""
        value=(kullanici_ID,isim,e_mail,uyelik_turu)
        cursor.execute(insertQuery,value)
        connection.commit()
        result=cursor.fetchmany(size=4)
        
        
    except Error as e:
        print("Error occured",e)
      
    finally:
        if(connection.is_connected()):
            connection.close()
            print("Bilgiler Kaydı Tamamlandı")
           
       
##### PREMIUM REGISTER #####

def premium_account_register(isim,e_mail,password,kredi_karti,cvv,expd,uyelik_turu): 
    normal_account_register(isim,e_mail,password,uyelik_turu)
    kullanici_ID=get_kullanici_id(e_mail)

    uyelik_baslangic_tarihi = datetime.datetime.today()
    fark = datetime.timedelta(days=30)
    uyelik_bitis_tarihi = uyelik_baslangic_tarihi + fark
    uyelik_bitis_tarihi.strftime('%c')
    

    #3_ucretli_uyelik kayıtları
    host="localhost"
    user="root"
    password="1234"
    database="pdf_converter"
     
    try:
        connection=mysql.connector.connect(host=host,user=user,password=password,database=database)
        cursor=connection.cursor()
        #1_kullanici_giris kayıtları
        insertQuery="""INSERT into 3_ucretli_uyelik(kullanici_ID,uyelik_baslangic_tarihi,uyelik_bitis_tarihi,kredi_karti_no,cvv,son_kullanim_tarihi) value (%s,%s,%s,%s,%s,%s)"""
        value=(kullanici_ID,uyelik_baslangic_tarihi,uyelik_bitis_tarihi,kredi_karti,cvv,expd)
        cursor.execute(insertQuery,value)
        connection.commit()
        result=cursor.fetchmany(size=4)
        
        
    except Error as e:
        print("Error occured",e)
      
    finally:
        if(connection.is_connected()):
            connection.close()
            print("Premium Üye Bilgileri Kaydedildi")


def premium_date(current_user):
    host="localhost"
    user="root"
    password="1234"
    database="pdf_converter"
     
    #Kullanıcı adı kontrol
    mydb=mysql.connector.connect(host=host,user=user,password=password,database=database)
    cursor=mydb.cursor()
    cursor.execute("SELECT kullanici_ID,uyelik_baslangic_tarihi,uyelik_bitis_tarihi from 3_ucretli_uyelik where kullanici_ID='"+current_user+"'")
    results=cursor.fetchone()

    #Günü Tarihlere Bölme
    if(results):
        uyelik_baslangic_tarihi = results[1]
        uyelik_bitis_tarihi = results[2]

        gun,saat = results[2].split()
        day=gun.split("-")
        uyelik_bitis = datetime.datetime(int(day[0]), int(day[1]), int(day[2]))

        bugun = datetime.datetime.today()
        fark=uyelik_bitis-bugun
        if(int(fark.days<=0)):
             return 0

        return uyelik_baslangic_tarihi,uyelik_bitis_tarihi,fark.days
    else:
        return 0
    
#KULLANICI HESABI SİLME (TRIGGER)
def delete_acc(current_user):
    host="localhost"
    user="root"
    password="1234"
    database="pdf_converter"
    mydb=mysql.connector.connect(host=host,user=user,password=password,database=database)
    cursor=mydb.cursor()
    query="DELETE FROM 1_kullanici_giris WHERE kullanici_ID=%s"
    cursor.execute(query,[(current_user)])
    mydb.commit()
    print(current_user + " No'lu Kullanıcının Üyeliği Silindi")

def delete_info(current_user):
    host="localhost"
    user="root"
    password="1234"
    database="pdf_converter"
    mydb=mysql.connector.connect(host=host,user=user,password=password,database=database)
    cursor=mydb.cursor()
    query="DELETE FROM 2_bilgiler WHERE kullanici_ID=%s"
    cursor.execute(query,[(current_user)])
    mydb.commit()
    print(current_user + " No'lu Kullanıcının Bilgileri Silindi")

def delete_pdf(current_user):
    host="localhost"
    user="root"
    password="1234"
    database="pdf_converter"
    mydb=mysql.connector.connect(host=host,user=user,password=password,database=database)
    cursor=mydb.cursor()
    query="DELETE FROM pdfler WHERE kullanici_ID=%s"
    cursor.execute(query,[(current_user)])
    mydb.commit()
    print(current_user + " No'lu Kullanıcının Pdfleri Silindi")
    

#TRIGGER OLUŞUMU
def trigger(current_user):
    host="localhost"
    user="root"
    password="1234"
    database="pdf_converter"
    mydb=mysql.connector.connect(host=host,user=user,password=password,database=database)
    cursor=mydb.cursor()

    #BİLGİLERİ ÇEKME
    query="SELECT * from 2_bilgiler WHERE kullanici_ID=%s"
    cursor.execute(query,[(current_user)])
    giris_kontrol=cursor.fetchone()
   
    #Z_SİLİNMİS_BİLGİLER TRIGGER
    insertQuery="""INSERT into z_silinmis_bilgiler(kullanici_ID,kullanici_isim_soyisim,kullanici_mail,kullanici_uyelik_duzeyi) value (%s,%s,%s,%s)"""
    value=(giris_kontrol[0],giris_kontrol[1],giris_kontrol[2],giris_kontrol[3])
    cursor.execute(insertQuery,value)
    mydb.commit()
    result=cursor.fetchmany(size=4)
    trigger_1(current_user)


def trigger_1(current_user):
    host="localhost"
    user="root"
    password="1234"
    database="pdf_converter"
    mydb=mysql.connector.connect(host=host,user=user,password=password,database=database)
    cursor=mydb.cursor()

    #BİLGİLERİ ÇEKME
    query="SELECT pdf_ID,pdf_adi,kullanici_ID,pdf_data from pdfler WHERE kullanici_ID=%s"
    cursor.execute(query,[(current_user)])
    giris_kontrol=cursor.fetchall()
    
    #Z_SİLİNMİS_PDFLER TRIGGER
    insertQuery="""INSERT into z_silinmis_pdfler(pdf_ID,pdf_adi,kullanici_ID,pdf_data) value (%s,%s,%s,%s)"""
    value=(giris_kontrol[0][0],giris_kontrol[0][1],giris_kontrol[0][2],giris_kontrol[0][3])
    cursor.execute(insertQuery,value)
    mydb.commit()
    result=cursor.fetchmany(size=4)
    
    delete_info(current_user)
    delete_pdf(current_user)
    delete_acc(current_user)
    
    
    

