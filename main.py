#from time import sleep
from turtle import goto
import cv2
import shutil
import requests
from PIL import Image
import time
a = 177
s="22" 


my_url = 'link anh 1'
response = requests.get(my_url, stream=True)
with open('my_image.ipg', 'wb') as file:
    shutil.copyfileobj(response.raw, file)
del response
response2 = requests.get('link anh 2', stream=True)
with open('my_image2.ipg', 'wb') as file:
    shutil.copyfileobj(response2.raw, file)
del response2
response3 = requests.get('link anh 3', stream=True)
with open('my_image3.ipg', 'wb') as file:
    shutil.copyfileobj(response3.raw, file)
del response3
so_do= cv2.imread("my_image.ipg")
so_do2= cv2.imread("my_image2.ipg")
so_do3= cv2.imread("my_image3.ipg")

img_resized = cv2.resize(src=so_do, dsize=(540,720 ))
img_resized2 = cv2.resize(src=so_do2, dsize=(540,720 ))
img_resized3 = cv2.resize(src=so_do3, dsize=(540,720 ))
def nhap():
    print("Hay nhap pass de bat dau.")
    global s
    s=input()
nhap()

def inchu():
    f = open('myfile.txt', "r")
    for i in range(255):
        with open('myfile.txt', 'r') as f:
            datalist = f.readlines() 
            line2 = datalist[i]
            print(line2)
            time.sleep(0.07)
while s !="24062003":#pass muon nhap
    nhap()
else:
    inchu()
print("nhan enter de tiep tuc")
c=input()
time.sleep(1)

cv2.imshow(' ',img_resized)
cv2.imshow('  ',img_resized2 )
cv2.imshow('   ',img_resized3 )
cv2.waitKey()
print("-------------------------------------------------------")
input()
ky=cv2.waitKey(1)
if ky==27:
    cv2.destroyAllWindows()
    

