CREATE FUNCTION kayitsayi(gelensayi INTEGER)
RETURNS INTEGER
BEGIN
SELECT count(pdf_adi)
FROM pdfler 
WHERE
    kullanici_ID = gelensayi;
RETURN count(pdf_adi);
END;