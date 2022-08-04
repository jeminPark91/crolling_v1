from turtle import position
import pyautogui as pgi
import time
import keyboard

position = ""

print('마우스 돌아올 위치지정 "F2" 를 눌려주세요')
while position == "":
    if keyboard.is_pressed('F2'):
        position = pgi.position()
        print(position)
        break
    else:
        pass

def imgclick(files): #이미지 찾아서 클릭 함수
    imgfile = pgi.locateCenterOnScreen(files, confidence = 0.7)

print('"F3" 번역시작 / "F4" 10초 누르면 중지')
while True:
    if keyboard.is_pressed('F3'): #작업시작
        print('작업시작')
        print(position)

        while True:
            endimg = pgi.locateCenterOnScreen('end.png')

            if keyboard.is_pressed('F4'): #F4 중지
                print('중지됨 / 다시시작 F4')
                break
            else:
                if endimg == None:
                    print('번역중...')
                    pgi.press('pgdn')
                    time.sleep(1)
                    pgi.rightClick()
                    time.sleep(1)
                    transimg = pgi.locateCenterOnScreen('transword.png')
                    pgi.click(transimg)
                    time.sleep(3)
                    pgi.moveTo(position)
                else:
                    print('작업 끝 \n 다시시작 F3')
                    pgi.press('home')
                    break