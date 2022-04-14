from time import sleep
from types import NoneType

import pyautogui
import pyautogui as pg
from PIL import ImageGrab
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\valer\\AppData\\Roaming\\Tesseract-OCR\\tesseract.exe"  # needed for Windows as OS
first_name = "FINIZIOLUCA"
first_letter_pos = 0


def getNome(strings, index, left_list):
    count = 0
    out = ""
    for char in strings[index::]:
        if char.isupper() or char == '\'':
            out += char
        else:
            break
        if (count > 0 and left_list[index + count + 1] - left_list[index + count] > 80):
            break
        elif (count > 0 and left_list[index + count + 1] - left_list[index + count] > 22):
            out+=' '
        count += 1

    return out


matricole = []
with open('values.txt') as f:
    for line in f.readlines():
        matricole.append(line.split(" -->")[0])

sleep(3)
clk = pg.locateOnScreen('inputbox001.png', confidence=0.7)
box=pg.locateOnScreen('inputbox002.png', confidence=0.7)
nomi = []
for matricola in matricole:
    pg.click(x=clk.left + int(clk.width / 2), y=clk.top + int(clk.height / 2))
    # Holds down the alt key
    pyautogui.keyDown("ctrl")
    pyautogui.press("a")
    pyautogui.keyUp("ctrl")
    pyautogui.press("backspace")

    pyautogui.write('S' + matricola)
    sleep(1)
    screen = ImageGrab.grab(bbox=(box.left+box.width*0.17,box.top+box.height*1.2,box.left+box.width*0.8,box.top+box.height*2.2))
    screen.save(matricola+'.png')
    cap = screen.convert('L')  # make grayscale

    data = pytesseract.image_to_boxes(cap, output_type=Output.DICT)
    chars=dict(data).get('char')
    if(type(chars)!=NoneType):
        strings = ''.join(chars)
        nome = strings
    else:
        nome="not found"

    nomi.append(nome)
    print(matricola, " --> ", nome)
