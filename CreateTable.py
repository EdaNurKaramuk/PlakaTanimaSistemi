#
#           SAKARYA ÜNİVERSİTESİ BİLGİSAYAR VE BİLİŞİM BİLİMLERİ FAKÜLTESİ
#                           BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ
#               BİLGİSAYAR MÜHENDİSLİĞİ TASARIMI - 2. ÖĞRETİM P GRUBU
#           EDA NUR KARAMUK - G181210061 & ELİF RUMEYSA AYDIN - G181210031
#
#

import sqlite3 as sql

def main():
    try:
        db = sql.connect('Database/PlateRecognition.db')
        cur = db.cursor()
        tablequery = "CREATE TABLE PlateNumberInformations (plate_number varchar(20) NOT NULL PRIMARY KEY UNIQUE, name varchar(20) NOT NULL, surname varchar(20) NOT NULL, address varchar(100) NOT NULL, phone_number varchar(11) NOT NULL, email_address varchar(50))"
        cur.execute(tablequery)
        print("Tablo başarılı bir şekilde oluşturuldu.")

    except sql.Error as e:
        print("Bu tablo zaten var veya bir hata oluştu.")

    finally:
        db.close()


if __name__ == "__main__":
    main()