#
#           SAKARYA ÜNİVERSİTESİ BİLGİSAYAR VE BİLİŞİM BİLİMLERİ FAKÜLTESİ
#                           BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ
#               BİLGİSAYAR MÜHENDİSLİĞİ TASARIMI - 2. ÖĞRETİM P GRUBU
#           EDA NUR KARAMUK - G181210061 & ELİF RUMEYSA AYDIN - G181210031
#
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap
import cv2, imutils
import sqlite3 as sql
import os
os.system('python Connection.py')
os.system('python CreateTable.py')
from PlateRecognitionAlgorithm import plateRecognize
from PlateRecords import Ui_SecondWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1065, 594)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(226, 226, 226);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon/car.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plate_result = QtWidgets.QGroupBox(self.centralwidget)
        self.plate_result.setGeometry(QtCore.QRect(550, 10, 481, 551))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plate_result.setFont(font)
        self.plate_result.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.plate_result.setObjectName("plate_result")
        self.label_PlateResult = QtWidgets.QLabel(self.plate_result)
        self.label_PlateResult.setGeometry(QtCore.QRect(10, 40, 461, 351))
        self.label_PlateResult.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.label_PlateResult.setText("")
        self.label_PlateResult.setAlignment(QtCore.Qt.AlignCenter)
        self.label_PlateResult.setObjectName("label_PlateResult")
        self.textPlateResult = QtWidgets.QTextEdit(self.plate_result)
        self.textPlateResult.setGeometry(QtCore.QRect(10, 400, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textPlateResult.setFont(font)
        self.textPlateResult.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textPlateResult.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textPlateResult.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textPlateResult.setReadOnly(True)
        self.textPlateResult.setObjectName("textPlateResult")
        self.textEdit = QtWidgets.QTextEdit(self.plate_result)
        self.textEdit.setGeometry(QtCore.QRect(10, 480, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.btnCheckPlateNumber = QtWidgets.QPushButton(self.plate_result)
        self.btnCheckPlateNumber.setGeometry(QtCore.QRect(290, 400, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnCheckPlateNumber.setFont(font)
        self.btnCheckPlateNumber.setStyleSheet("background-color: rgb(79, 79, 79);\n"
"color: rgb(255, 255, 255);")
        self.btnCheckPlateNumber.setIconSize(QtCore.QSize(30, 30))
        self.btnCheckPlateNumber.setObjectName("btnCheckPlateNumber")
        self.btnShowPlateRecords = QtWidgets.QPushButton(self.plate_result)
        self.btnShowPlateRecords.setGeometry(QtCore.QRect(290, 480, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnShowPlateRecords.setFont(font)
        self.btnShowPlateRecords.setStyleSheet("background-color: rgb(79, 79, 79);\n"
"color: rgb(255, 255, 255);")
        self.btnShowPlateRecords.setIconSize(QtCore.QSize(30, 30))
        self.btnShowPlateRecords.setObjectName("btnShowPlateRecords")
        self.vehicle_plate = QtWidgets.QGroupBox(self.centralwidget)
        self.vehicle_plate.setGeometry(QtCore.QRect(30, 10, 481, 551))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vehicle_plate.setFont(font)
        self.vehicle_plate.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.vehicle_plate.setObjectName("vehicle_plate")
        self.startPlateRecognition = QtWidgets.QPushButton(self.vehicle_plate)
        self.startPlateRecognition.setGeometry(QtCore.QRect(250, 430, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.startPlateRecognition.setFont(font)
        self.startPlateRecognition.setStyleSheet("background-color: rgb(79, 79, 79);\n"
"color: rgb(255, 255, 255);")
        self.startPlateRecognition.setIconSize(QtCore.QSize(30, 30))
        self.startPlateRecognition.setObjectName("startPlateRecognition")
        self.labelVehicle = QtWidgets.QLabel(self.vehicle_plate)
        self.labelVehicle.setGeometry(QtCore.QRect(10, 30, 461, 351))
        self.labelVehicle.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.labelVehicle.setText("")
        self.labelVehicle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelVehicle.setObjectName("labelVehicle")
        self.openImageFile = QtWidgets.QPushButton(self.vehicle_plate)
        self.openImageFile.setGeometry(QtCore.QRect(20, 430, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.openImageFile.setFont(font)
        self.openImageFile.setStyleSheet("background-color: rgb(79, 79, 79);\n"
"color: rgb(255, 255, 255);")
        self.openImageFile.setIconSize(QtCore.QSize(30, 30))
        self.openImageFile.setObjectName("openImageFile")
        self.vehicle_plate.raise_()
        self.plate_result.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.openImageFile.clicked.connect(self.loadImage)
        self.startPlateRecognition.clicked.connect(self.showPlateRecognition)
        self.btnShowPlateRecords.clicked.connect(self.openWindow)
        self.btnCheckPlateNumber.clicked.connect(self.checkPlateNumber)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    imagePath = ""
    def loadImage(self):
        """ Bilgisayardan resim seçilmesini sağlayan fonksiyon.
        """
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.png *.xmp *.jpg *.jpeg *.webp)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image)
        global imagePath
        imagePath = self.image

    def setPhoto(self, image):
        """ Label bileşeninde resmin yeniden boyutlandırıp gösterilmesini sağlayan fonksiyon.
        """
        self.tmp = image
        image = imutils.resize(image, width=500)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.labelVehicle.setPixmap(QtGui.QPixmap.fromImage(image))

    # Plaka Okuma butonuna tıklandığında çalışan fonksiyon.
    def showPlateRecognition(self):
        self.writePlate(imagePath)
        self.showPlateImage(imagePath)

    # Plaka Okuma algoritmasında resmin sonuç label üzerinde gösterilmesini sağlayan fonksiyon.
    def showPlateImage(self, image):
        self.tmp = image
        txt, krp = plateRecognize(image)
        krp = imutils.resize(krp, width=350)
        frame = cv2.cvtColor(krp, cv2.COLOR_BGR2RGB)
        krp = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.label_PlateResult.setPixmap(QtGui.QPixmap.fromImage(krp))

    # Plaka Okuma algoritmasında palaka metninin sonuç textBox'ın üzerinde gösterilmesini sağlayan fonksiyon.
    def writePlate(self, image):
        txt, krp = plateRecognize(image)
        self.textPlateResult.setText(txt)

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.plateResult = self.textPlateResult.toPlainText()
        self.ui = Ui_SecondWindow(self.plateResult)
        self.ui.setupUi(self.window)
        self.window.show()

    def checkPlateNumber(self):
        plateNumber = self.textPlateResult.toPlainText()

        self.conn = sql.connect("Database/PlateRecognition.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM PlateNumberInformations WHERE plate_number = ?",(plateNumber,))
        data = self.c.fetchall()
        if len(data) == 0:
            self.textEdit.setText("Araç kayıtlı değil.")
        else:
            self.textEdit.setText("Araç kayıtlı.")
        self.conn.commit()
        self.c.close()
        self.conn.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plaka Tanıma Sistemi"))
        self.plate_result.setTitle(_translate("MainWindow", "Plaka Sonucu"))
        self.btnCheckPlateNumber.setText(_translate("MainWindow", "Plakayı Kontrol Et"))
        self.btnShowPlateRecords.setText(_translate("MainWindow", "Plaka Kayıtlarını Göster"))
        self.vehicle_plate.setTitle(_translate("MainWindow", "Araç/Plaka Görseli"))
        self.startPlateRecognition.setText(_translate("MainWindow", "Plaka Okuma Başlat"))
        self.openImageFile.setText(_translate("MainWindow", "Resim Dosyası Seç"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
