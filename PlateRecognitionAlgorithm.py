#
#           SAKARYA ÜNİVERSİTESİ BİLGİSAYAR VE BİLİŞİM BİLİMLERİ FAKÜLTESİ
#                           BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ
#               BİLGİSAYAR MÜHENDİSLİĞİ TASARIMI - 2. ÖĞRETİM P GRUBU
#           EDA NUR KARAMUK - G181210061 & ELİF RUMEYSA AYDIN - G181210031
#
#

import cv2 # pip install opencv-python
import imutils # pip install imutils
import numpy as np # pip install numpy
import pytesseract # pip install pytesseract
import re


def plateRecognize(imgparam):

    # https://tesseract-ocr.github.io/tessdoc/Downloads.html
    #https://digi.bib.uni-mannheim.de/tesseract/

    # imgparam -> Arayüzden seçilen görselin yolu parametre olarak burada kullanılır.
    img = imgparam
    img = cv2.resize(img, (800,500))
    # Eğer sabit bir yerde plaka okuyacak ise daha optimize
    #olması için resmin kırpılması

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Resmi alıp griye çeviriyor.
    gray = cv2.bilateralFilter(gray, 13, 15, 15)
    #(source_image, diameter of pixel, sigmaColor, sigmaSpace)

    cany = cv2.Canny(gray, 30, 200) # 30, 200 yoğunluk min ve max
    #cany edge kenar algılama algoritması

    # Kontür alma
    contours = cv2.findContours(cany.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contours = imutils.grab_contours(contours)
    #Tersten sıralama yaptırıyoruz ve ilk 10 değeri çekiyoruz.
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
    screenCnt = 0

    for c in contours: # -> https://stackoverflow.com/questions/62274412/cv2-approxpolydp-cv2-arclength-how-these-works

        _ = cv2.arcLength(c, True)
        #https://docs.opencv.org/master/d3/dc0/group__imgproc__shape.html#ga8d26483c636be6b35c3ec6335798a47c
        approx = cv2.approxPolyDP(c, 0.018 * _, True)
        #Daha düzgün dikdörtgen algılatmak
        # Dörtgen bir cisim
        if len(approx) == 4:
            screenCnt = approx
            break

    if screenCnt is None:
        detected = 0
    else:
        detected = 1  #Eğer varsa

    if detected == 1:
        cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3) # Kontür çizilir.

    # Numara plakası dışındaki kısmı maskeleme
    mask = np.zeros(gray.shape,np.uint8)
    #shape = satır sütun piksel sayısı ve renkli ise renk katmanları
    #np.uint8 = Unsigned integer (0 to 255)
    #np.zeros = np.zeros() bir tuple (demet) değeri alır.
    #Bu tuple değeri, oluşturmak istediğimiz dizinin boyutlarının değerleridir.

    new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
    new_image = cv2.bitwise_and(img,img,mask=mask)
    #https://stackoverflow.com/questions/44333605/what-does-bitwise-and-operator-exactly-do-in-opencv/52429616
    #algılanan resmin dışındakileri siyah yapar


    (x, y) = np.where(mask == 255)
    #np.where(mask<5,-1,100) şeklinde çalışsaydı eğer
    #koşulu sağlamadığında -1 değerini atayacak sağladığında 100
    #np.where(mask==255) olduğunda ise true false döndürecek

    (tx, ty) = (np.min(x), np.min(y)) # Dizinin minimum ve maksimum elemanını buluyor.
    (bx, by) = (np.max(x), np.max(y))
    Cropped = gray[tx:bx+1, ty:by+1] #tx = bx + 1 kadar, ty=by +1 kadar
    custom_config = r'-l eng --psm 6' #config l dil kodu --psm
    text = pytesseract.image_to_string(Cropped, config=custom_config)
    # Plaka yazısını okuma

    #Özel karakterlerin plakadan kaldırılması.
    plateNoFix = text.replace("\n","")
    plateNoFix2 = plateNoFix.replace("\f", "")
    plateNoFix3 = plateNoFix2.strip("#")
    resultPlateText = re.sub('[()"{}<>!-]', '', plateNoFix3)
    img = cv2.resize(img,(500,300))
    Cropped = cv2.resize(Cropped,(200,70))

    return resultPlateText, Cropped


