import sqlite3
import function

db=sqlite3.connect("Odev.db") ## Odev.db adlı veri tabanına bağlanır yoksa oluşturur
### db=sqlite3.connect("C:/Users/tolga/Desktop/Büyük Veri Ödev/Odev.db")
imlec=db.cursor()

kmt="CREATE TABLE IF NOT EXISTS veriler(ad,soyad,yas)" ## veriler adında tablo yoksa oluşturur ve ad,soyad,yas sutunlarını ekler
imlec.execute(kmt)

"""

kmt="INSERT INTO veriler VALUES('Eray','Küçük',24)" ## veriler tablosuna sırayla  girilen ad,soyad,yas verilerini ekler
bilgiler=function.listele(db,kmt)

"""
"""

kmt="Select * from veriler"
bilgiler=function.listele(db,kmt).fetchall() ## veriler tablosundaki bütün verileri listeler
print(bilgiler)

"""
"""

kmt="Select * from veriler where yas={}".format(24) ## veriler tablosunda yası 24 olan verilerin istenilen bilgilerin, ekrana yazdırır
bilgi=function.parametreliliste(db,kmt).fetchone()

print("İsim :"+str(bilgi[0]))
print("Soyisim :"+str(bilgi[1]))
print("Yaş :"+str(bilgi[2]))

"""
"""

kmt="UPDATE veriler SET yas ={} where ad={}".format(28,'Tolga') ## veriler tablosunda adı 'Tolga'olan verinin yasını 28 yapar
bilgi=function.parametreliliste(db,kmt)

"""
"""

kmt="Delete from veriler where yas={}".format(80) ## veriler tablosunda yası 80 olan verileri siler
bilgi=function.parametreliliste(db,kmt)

"""
"""
kmt="Select * from veriler"
bilgiler=function.listele(db,kmt).fetchall()
print(bilgiler)

"""

db.close()
