import pyshorteners
import qrcode
import cv2
from pyzbar import pyzbar

def qrcode():

    action1 = int(input(" What to do? (1.Make qrcode 2.Decrypt qrcode) "))

    if action1 == 1:
        URL = input(" URL: ")
        file = input(" Enter file name:")

        filename = file +".png"

        img = qrcode.make(URL)
        img.save(filename)
        
    elif action1 == 2:
        image_name = input(" Image: ")

        img = cv2.imread(image_name)
        barcodes = pyzbar.decode(img)

        for barcode in barcodes:
            barcodeData = barcode.data.decode('utf-8')
            print(f" Text:  {barcodeData}")
    
    else:
        print (" ERROR ")

def shroturl():
    url = input(" URL: ")
    n = input(" Choice service ( 1:Os.db, 2:Chilp.it, 3:Da.gd, 4:Qps.ru, 5:TinyURL.com):  ")

    if n == str(1):
        s = pyshorteners.Shortener()
        f = s.osdb.short(url)
        print(" Short URL: ",f)
    elif n == str(2):
        s = pyshorteners.Shortener()
        short_url = s.chilpit.short(url)
        print(" Short URL: ",short_url)
    elif n == str(3):
        s = pyshorteners.Shortener()
        abz = s.dagd.short(url)
        print(" Short URL: ",abz)
    elif n == str(4):
        s = pyshorteners.Shortener()
        abh = s.qpsru.short(url)
        print(" Short URL: ",abh)
    elif n == str(5):
        s = pyshorteners.Shortener()
        abk = s.tinyurl.short(url)
        print(" Short URL: ",abk)
    else:
        print (" ERROR ")

action = int(input(" What to do? (1.QrCode 2.ShortUrl) "))

if (int(action) == 1):
    qrcode()

elif (int(action) == 2):
    shroturl()
