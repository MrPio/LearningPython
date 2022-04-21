import datetime
import os

import pyautogui

import AutoLogonRun

os.startfile('teams.lnk')
btn = AutoLogonRun.wait_for_element_appear('ui/ch_em.png', 1)
if btn is not None:
    AutoLogonRun.click_center(btn)
weekday = datetime.datetime.today().weekday()
image = ''
if weekday == 1:
    image = r'ui\em_lez_mar.png'
elif weekday == 2:
    image = r'ui\em_lez_mer.png'
elif weekday == 4:
    image = r'ui\em_lez_ven.png'
else:
    exit(0)
btn = AutoLogon.wait_for_element_appear(image)
pyautogui.sleep(1)
AutoLogon.click_center(btn)
pyautogui.sleep(1)