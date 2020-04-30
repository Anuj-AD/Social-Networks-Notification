# thie program will use webbrowser to go through your social networking
# sites and give you a brief about the messages and notifications
import webbrowser
import pyautogui as pg
import time
import pytesseract as pt
import cv2


url1 = "https://www.quora.com/"
url2 = "https://www.instagram.com/"
url3 = "https://www.fb.com/"
path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
webbrowser.get(path).open(url1)
time.sleep(10)
image = pg.screenshot("ss.png")
ansL = pg.locateOnScreen("QAns.png", confidence = 0.8)
pg.moveTo(ansL)
pg.move(61,-19)
cdtx, cdty = pg.position()
ansT = pg.screenshot('ansT.png',region = (cdtx,cdty,14,11))
notL = pg.locateOnScreen("QNot.png", confidence = 0.8)
pg.moveTo(notL)
pg.move(97,-19)
cdtx, cdty = pg.position()
notT = pg.screenshot('notT.png',region = (cdtx,cdty,14,11))
otL = pg.locateOnScreen("QMore.png", confidence = 0.8)
pg.moveTo(otL)
pg.move(2,-23)
cdtx, cdty = pg.position()
otT = pg.screenshot('moreT.png',region = (cdtx,cdty,14,11))
#count number of ans Notifications
ansN = cv2.imread('ansT.png', cv2.IMREAD_GRAYSCALE)
ansN = cv2.resize(ansN, (0,0), fx = 5, fy = 5)
ret,thresh = cv2.threshold(ansN, 10, 255, cv2.THRESH_OTSU)
ansN = pt.image_to_string(thresh, config = " --psm 10")
#count number of not Notifications
notN = cv2.imread('notT.png', cv2.IMREAD_GRAYSCALE)
notN = cv2.resize(notN, (0,0), fx = 5, fy = 5)
ret,thresh = cv2.threshold(notN, 10, 255, cv2.THRESH_OTSU)
notN = pt.image_to_string(thresh, config = " --psm 10")
#count number of more Notifications
moreN = cv2.imread('moreT.png', cv2.IMREAD_GRAYSCALE)
moreN = cv2.resize(moreN, (0,0), fx = 4.5, fy = 5)
ret,thresh = cv2.threshold(moreN, 10, 255, cv2.THRESH_OTSU)
moreN = pt.image_to_string(thresh, config = " --psm 10")
try:
    ansN = int(ansN)
except:
    ansN = 0
try:
    notN = int(notN)
except:
    notN = 0
try:
    moreN = int(moreN)
except:
    moreN = 0
print('QUORA: You have')
print(ansN, end = '')
print(' Answer Request(s)')
print(notN, end = '')
print(' Notification(s)')
print(moreN, end = '')
print(' Notification(s) in other Languages')
time.sleep(3)

#facebook
webbrowser.get(path).open(url3)
time.sleep(10)
image = pg.screenshot("ss.png")
ansL = pg.locateOnScreen("FMsg.png", confidence = 0.8)
pg.moveTo(ansL)
pg.move(7,-18)
cdtx, cdty = pg.position()
ansT = pg.screenshot('fansT.png',region = (cdtx,cdty,11,9))
ansN = cv2.imread('fansT.png', cv2.IMREAD_GRAYSCALE)
ansN = cv2.resize(ansN, (0,0), fx = 5, fy = 5)
ret,thresh = cv2.threshold(ansN, 10, 255, cv2.THRESH_OTSU)
ansN = pt.image_to_string(thresh, config = " --psm 10")
try:
    ansN = int(ansN)
except:
    ansN = 0
notL = pg.locateOnScreen("FMsg.png", confidence = 0.8)
pg.moveTo(notL)
pg.move(39,-19)
cdtx, cdty = pg.position()
notT = pg.screenshot('fnotT.png',region = (cdtx,cdty,14,11))
notN = cv2.imread('fnotT.png', cv2.IMREAD_GRAYSCALE)
notN = cv2.resize(notN, (0,0), fx = 5, fy = 5)
ret,thresh = cv2.threshold(notN, 10, 255, cv2.THRESH_OTSU)
notN = pt.image_to_string(thresh, config = " --psm 10")
try:
    notN = int(notN)
except:
    notN = 0
print('FACEBOOK: You have')
print(ansN, end = '')
print(' Message(s)')
print(notN, end = '')
print(' Notification(s)')
time.sleep(3)

#instagram
webbrowser.get(path).open(url2)
time.sleep(10)
image = pg.screenshot("ss.png")
ansL = pg.locateOnScreen("IMsg.png", confidence = 0.8)
pg.moveTo(ansL)
pg.move(11,-9)
cdtx, cdty = pg.position()
ansT = pg.screenshot('iansT.png',region = (cdtx,cdty,11,10))
ansN = cv2.imread('iansT.png', cv2.IMREAD_GRAYSCALE)
ansN = cv2.resize(ansN, (0,0), fx = 5, fy = 5)
ret,thresh = cv2.threshold(ansN, 10, 255, cv2.THRESH_OTSU)
ansN = pt.image_to_string(thresh, config = " --psm 10")
try:
    ansN = int(ansN)
except:
    ansN = 0
notL = pg.locateOnScreen("INot.png", confidence = 0.99)
msg = 'New'
if notL == None:
    msg = 'No'
print('INSTAGRAM: You have')
print(ansN, end = '')
print(' Message(s)')
print(msg, end = '')
print(' Notification(s)')
