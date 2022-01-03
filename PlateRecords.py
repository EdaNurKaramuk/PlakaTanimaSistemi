#
#           SAKARYA ÜNİVERSİTESİ BİLGİSAYAR VE BİLİŞİM BİLİMLERİ FAKÜLTESİ
#                           BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ
#               BİLGİSAYAR MÜHENDİSLİĞİ TASARIMI - 2. ÖĞRETİM P GRUBU
#           EDA NUR KARAMUK - G181210061 & ELİF RUMEYSA AYDIN - G181210031
#
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem
import sqlite3 as sql
import os
os.system('python Connection.py')
os.system('python CreateTable.py')


class Ui_SecondWindow(object):
    def __init__(self, plateResult):
        self.plateResultText = plateResult
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(910, 723)
        SecondWindow.setStyleSheet("background-color: rgb(250, 250, 250);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon/car.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        SecondWindow.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(560, 20, 211, 41))
        self.btnSave.setObjectName("btnSave")
        self.btnSave.setStyleSheet("background-color: rgb(79, 79, 79);\n""color: rgb(255, 255, 255);")
        self.btnSave.setFont(font)
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setGeometry(QtCore.QRect(560, 70, 211, 41))
        self.btnDelete.setObjectName("btnDelete")
        self.btnDelete.setStyleSheet("background-color: rgb(79, 79, 79);\n""color: rgb(255, 255, 255);")
        self.btnDelete.setFont(font)
        self.btnUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdate.setGeometry(QtCore.QRect(560, 120, 211, 41))
        self.btnUpdate.setObjectName("btnUpdate")
        self.btnUpdate.setStyleSheet("background-color: rgb(79, 79, 79);\n""color: rgb(255, 255, 255);")
        self.btnUpdate.setFont(font)
        self.btnListAll = QtWidgets.QPushButton(self.centralwidget)
        self.btnListAll.setGeometry(QtCore.QRect(560, 170, 211, 41))
        self.btnListAll.setObjectName("btnListAll")
        self.btnListAll.setStyleSheet("background-color: rgb(79, 79, 79);\n""color: rgb(255, 255, 255);")
        self.btnListAll.setFont(font)
        font.setPointSize(9)
        self.txtPlateNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPlateNumber.setGeometry(QtCore.QRect(220, 20, 311, 41))
        self.txtPlateNumber.setObjectName("txtPlateNumber")
        self.txtPlateNumber.setFont(font)
        self.txtName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtName.setGeometry(QtCore.QRect(220, 70, 311, 41))
        self.txtName.setObjectName("txtName")
        self.txtName.setFont(font)
        self.txtSurname = QtWidgets.QLineEdit(self.centralwidget)
        self.txtSurname.setGeometry(QtCore.QRect(220, 120, 311, 41))
        self.txtSurname.setObjectName("txtSurname")
        self.txtSurname.setFont(font)
        self.txtAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAddress.setGeometry(QtCore.QRect(220, 170, 311, 41))
        self.txtAddress.setObjectName("txtAddress")
        self.txtAddress.setFont(font)
        self.txtPhoneNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPhoneNumber.setGeometry(QtCore.QRect(220, 220, 311, 41))
        self.txtPhoneNumber.setObjectName("txtPhoneNumber")
        self.txtPhoneNumber.setFont(font)
        self.txtEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.txtEmail.setGeometry(QtCore.QRect(220, 270, 311, 41))
        self.txtEmail.setObjectName("txtEmail")
        self.txtEmail.setFont(font)
        font.setPointSize(10)
        self.lblPlateNumber = QtWidgets.QLabel(self.centralwidget)
        self.lblPlateNumber.setGeometry(QtCore.QRect(10, 20, 201, 41))
        self.lblPlateNumber.setObjectName("lblPlateNumber")
        self.lblPlateNumber.setFont(font)
        self.lblName = QtWidgets.QLabel(self.centralwidget)
        self.lblName.setGeometry(QtCore.QRect(10, 70, 201, 41))
        self.lblName.setObjectName("lblName")
        self.lblName.setFont(font)
        self.lblSurname = QtWidgets.QLabel(self.centralwidget)
        self.lblSurname.setGeometry(QtCore.QRect(10, 120, 201, 41))
        self.lblSurname.setObjectName("lblSurname")
        self.lblSurname.setFont(font)
        self.lblAddress = QtWidgets.QLabel(self.centralwidget)
        self.lblAddress.setGeometry(QtCore.QRect(10, 170, 201, 41))
        self.lblAddress.setObjectName("lblAddress")
        self.lblAddress.setFont(font)
        self.lblPhoneNumber = QtWidgets.QLabel(self.centralwidget)
        self.lblPhoneNumber.setGeometry(QtCore.QRect(10, 220, 201, 41))
        self.lblPhoneNumber.setObjectName("lblPhoneNumber")
        self.lblPhoneNumber.setFont(font)
        self.lblEmailAddress = QtWidgets.QLabel(self.centralwidget)
        self.lblEmailAddress.setGeometry(QtCore.QRect(10, 270, 201, 41))
        self.lblEmailAddress.setObjectName("lblEmailAddress")
        self.lblEmailAddress.setFont(font)
        self.tblListele = QtWidgets.QTableWidget(self.centralwidget)
        self.tblListele.setGeometry(QtCore.QRect(10, 330, 891, 341))
        self.tblListele.setObjectName("tblListele")
        self.tblListele.setColumnCount(0)
        self.tblListele.setRowCount(0)
        font.setPointSize(8)
        self.tblListele.setFont(font)
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 22))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def btnClean(self):
        self.txtPlateNumber.clear()
        self.txtName.clear()
        self.txtSurname.clear()
        self.txtAddress.clear()
        self.txtPhoneNumber.clear()
        self.txtEmail.clear()

    def ListOnClick(self):
        self.txtPlateNumber.setText(self.tblListele.item(self.tblListele.currentRow(), 0).text())
        self.txtName.setText(self.tblListele.item(self.tblListele.currentRow(), 1).text())
        self.txtSurname.setText(self.tblListele.item(self.tblListele.currentRow(), 2).text())
        self.txtAddress.setText(self.tblListele.item(self.tblListele.currentRow(), 3).text())
        self.txtPhoneNumber.setText(self.tblListele.item(self.tblListele.currentRow(), 4).text())
        self.txtEmail.setText(self.tblListele.item(self.tblListele.currentRow(), 5).text())

    def btnSaveClick(self):
        id = self.txtPlateNumber.text()
        ad = self.txtName.text()
        soyad = self.txtSurname.text()
        adres = self.txtAddress.text()
        telefon = self.txtPhoneNumber.text()
        email = self.txtEmail.text()

        try:
            self.conn = sql.connect("Database/PlateRecognition.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO PlateNumberInformations VALUES (?,?,?,?,?,?)",
                           (id, ad, soyad, adres, telefon, email))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful -', 'Plaka bilgisi başarılı bir şekilde kaydedildi.')
        except Exception:
            print('Error -', 'Plaka bilgisi kaydedilemedi.')

        self.btnClean()
        self.btnListAllClick()

    def btnListAllClick(self):
        self.tblListele.clear()
        self.tblListele.setColumnCount(6)
        self.tblListele.setHorizontalHeaderLabels(('Plaka Numarası', 'Ad', 'Soyad', 'Adres', 'Telefon', 'E-mail'))
        self.tblListele.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        db = sql.connect('Database/PlateRecognition.db')
        cur = db.cursor()
        selectquery = "SELECT * FROM PlateNumberInformations"
        cur.execute(selectquery)
        rows = cur.fetchall()

        self.tblListele.setRowCount(len(rows))

        for satirIndeks, satirVeri in enumerate(rows):
            for sutunIndeks, sutunVeri in enumerate(satirVeri):
                self.tblListele.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))

    def btnUpdateClick(self):
        id = self.txtPlateNumber.text()
        ad = self.txtName.text()
        soyad = self.txtSurname.text()
        adres = self.txtAddress.text()
        telefon = self.txtPhoneNumber.text()
        email = self.txtEmail.text()

        try:
            self.conn = sql.connect("Database/PlateRecognition.db")
            self.c = self.conn.cursor()
            self.c.execute("UPDATE PlateNumberInformations SET name = ?, surname = ?, address = ?, \
                phone_number = ?, email_address = ? WHERE plate_number = ?", (ad, soyad, adres, telefon, email, id))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful -', 'Plaka bilgisi başarılı bir şekilde güncellendi.')
        except Exception:
            print('Error -', 'Plaka bilgisi güncellenemedi.')

        self.btnClean()
        self.btnListAllClick()

    def btnDeleteClick(self):
        id = self.txtPlateNumber.text()

        try:
            self.conn = sql.connect("Database/PlateRecognition.db")
            self.c = self.conn.cursor()
            self.c.execute('DELETE FROM PlateNumberInformations WHERE plate_number = ?  ', (id,))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful -', 'Plaka bilgisi veri tabanından başarılı bir şekilde silindi.')
        except Exception:
            print('Error -', 'Plaka bilgisi veri tabanından silinemedi.')

        self.btnClean()
        self.btnListAllClick()

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "Araç Plaka Bilgileri"))
        self.btnSave.setText(_translate("SecondWindow", "KAYDET"))
        self.btnSave.clicked.connect(self.btnSaveClick)
        self.btnDelete.setText(_translate("SecondWindow", "SIL"))
        self.btnDelete.clicked.connect(self.btnDeleteClick)
        self.btnUpdate.setText(_translate("SecondWindow", "GUNCELLE"))
        self.btnUpdate.clicked.connect(self.btnUpdateClick)
        self.btnListAll.setText(_translate("SecondWindow", "LISTELE"))
        self.btnListAll.clicked.connect(self.btnListAllClick)
        self.tblListele.clicked.connect(self.ListOnClick)
        self.lblPlateNumber.setText(_translate("SecondWindow", "PLAKA NUMARASI"))
        self.lblName.setText(_translate("SecondWindow", "AD"))
        self.lblSurname.setText(_translate("SecondWindow", "SOYAD"))
        self.lblAddress.setText(_translate("SecondWindow", "ADRES"))
        self.lblPhoneNumber.setText(_translate("SecondWindow", "TELEFON"))
        self.lblEmailAddress.setText(_translate("SecondWindow", "E-MAIL"))
        self.txtPlateNumber.setText(_translate("SecondWindow", self.plateResultText))



