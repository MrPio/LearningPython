import datetime as dt
import os
import time
import webbrowser
from types import NoneType
import psutil
import pyautogui
import userpaths
from pynput.keyboard import Controller
import MrCrypto as Mc
from pywinauto import Application


def wait_for_element_appear(element_path: str, wait=8.0):
    start = time.time()
    while True:
        element = pyautogui.locateOnScreen(element_path)
        if time.time() - start > wait:
            print(f"I've waited too much! [{element_path}]")
            return None
        if type(element) is not NoneType:
            break
        pyautogui.sleep(0.5)
    return element


def click_center(element):
    pyautogui.click(x=element.left + int(element.width / 2),
                    y=element.top + int(element.height / 2))


def perform_login():
    mc = Mc.MrCrypto(userpaths.get_desktop() + "\\my.key")
    user = mc.decrypt(
        "gAAAAABiYCTHf3VnnhbmC_84uR_Kc04Lmh_Y36uul26Oi9atS3IPJpi1a7b2GdUVJu680_"
        "5aR-RshkGJ0jlCoLQTQ8YjvMnf2Q==")
    pwd = mc.decrypt(
        "gAAAAABiYCPgCNHBxNQ59Ruu2Ze5blUjLIfaURXjUScNP3Y7wPf5UxPzRIgXg_Eg-BOlem"
        "9QZyAPBm48ixyi_mSfiUGql2_MVg==")
    webbrowser.open('https://learn.univpm.it/', new=2)
    keyboard = Controller()
    pyautogui.sleep(0.1)
    login_button = wait_for_element_appear('ui\\login_btn.png')
    if login_button is None:
        return
    click_center(login_button)
    login_button_2 = wait_for_element_appear('ui\\login_btn_2.png')
    if login_button is None:
        return
    keyboard.type(user)
    pyautogui.press("tab")
    keyboard.type(pwd)
    click_center(login_button_2)
    pyautogui.sleep(0.5)


def maximize_current_window():
    pyautogui.hotkey('win', 'up')


def read_config(file_name: str) -> dict:
    config = {}
    config_text = open(file_name, 'r').read().replace('\n', '')
    config['course'] = []
    config['instructions'] = []

    for field in config_text.split('~')[0].split(';'):
        day_list = {}
        if (len(field) < 1):
            continue
        for day in field.split('=')[1].split(':'):
            day_list[int(day.split('-')[0])] = int(day.split('-')[1])
        config['course'].append(day_list)

    for course in config_text.split('~')[1::]:
        instructions = []
        for instr in course.split(';'):
            if len(instr) < 1:
                continue
            instructions.append({instr.split()[0]: instr.split()[-1]})
        config['instructions'].append(instructions)
    return config


def read_schedule(config: dict) -> list:
    weekday = dt.datetime.today().weekday()
    hour = dt.datetime.today().hour
    count = 0
    for course in config['course']:
        if dict(course).keys().__contains__(weekday) and \
                dict(course)[weekday] == hour:
            return config['instructions'][count]
        count += 1
    return []


def execute_instruction(code, value):
    if code == 'RUN':
        if '.lnk' in value:
            os.startfile(value)
        else:
            exec(open(value).read())
    elif code == 'CLICK':
        click_center(wait_for_element_appear(value))
    elif code == 'SLEEP':
        pyautogui.sleep(float(value))
    elif code == 'REC':
        bring_to_top(get_pid_by_name("obs64.exe"))
        click_center(wait_for_element_appear("ui\obs_rec.png"))
        bring_to_top(get_pid_by_name("Teams.exe"))


def bring_to_top(pid_list: []):
    for pid in pid_list:
        try:
            app = Application().connect(process=pid)
            app.top_window().set_focus()
            return
        except:
            pass


def get_pid_by_name(name: str):
    pid_list = []
    for process in psutil.process_iter():
        if process.name() == name:
            pid_list.append(process.pid)
    return pid_list


if __name__ == "__main__":
    config = read_config('config.txt')
    schedule = read_schedule(config)
    if "Teams.exe" not in (i.name() for i in psutil.process_iter()):
        os.startfile(r"teams.lnk")
        pyautogui.sleep(5)
    if "obs64.exe" not in (i.name() for i in psutil.process_iter()):
        os.startfile(r"obs.lnk")
        pyautogui.sleep(4)

    for instr in schedule:
        execute_instruction(list(instr.keys())[0], list(instr.values())[0])
