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
       print("Veri tabanı oluşturuldu.")
    except:
        print("Veri tabanı oluşturulamadı.")
    finally:
        db.close()

if __name__ == "__main__":
    main()