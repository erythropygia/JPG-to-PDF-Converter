DELIMITER //
CREATE TRIGGER hesap_silindi BEFORE DELETE
ON 1_kullanici_giris
FOR EACH ROW
BEGIN
  INSERT INTO z_silinmis_pdfler(pdf_ID,pdf_adi,kullanici_ID,pdf_data) values (pdf_ID,pdf_adi,kullanici_ID,pdf_data);
  INSERT INTO z_silinmis_bilgiler(kullanici_ID,kullanici_isim_soyisim,kullanici_mail,kullanici_uyelik_duzeyi) value (kullanici_ID,kullanici_isim_soyisim,kullanici_mail,kullanici_uyelik_duzeyi);
END//
DELIMITER ;