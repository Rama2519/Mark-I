import pyttsx3
import pyautogui as pag
from selenium import webdriver
from time import sleep as s
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import speech_recognition as sr
import os

opening = "opening"
playing = "playing"
alexa = "alexa"
listening = "How can I help you?: "
options = "Do you want me to play on YouTube or Amazon Music?"


def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)


def speak_text(x):
    # Initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(x)
    engine.runAndWait()


def convert(x):
    return x[0].split()


def list_to_string(x):
    str1 = " "
    return str1.join(x)


def music_amazon(x):
    pag.press("win")
    pag.write("amazon")
    pag.press("enter")
    s(0.5)
    pag.hotkey('win', 'up')
    s(3)
    pag.write(x)
    pag.press('enter')
    s(1)
    pag.moveTo(121, 475)
    pag.click()


def music_yt(x):
    yt = webdriver.Chrome(service=Service("C:/Users/ramas/chromedriver.exe"))
    yt.maximize_window()
    yt.get('https://www.youtube.com')
    s(0.5)
    pag.press("/")
    s(0.5)
    pag.write(x)
    pag.press("enter")
    s(1)
    yt.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div['
                              '1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div['
                              '2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]').click()
    while True:
        pass


def website(x):
    ws = webdriver.Chrome(service=Service("C:/Users/ramas/chromedriver.exe"))
    ws.maximize_window()
    ws.get('https://www.' + x + '.com')
    while True:
        pass


def open_app(x):
    pag.press("win")
    pag.write(x)
    pag.press("enter")


def my_music():
    open_app("amazon")
    s(3)
    pag.hotkey('win', 'up')
    pag.moveTo(531, 72)
    pag.click()
    pag.moveTo(507, 173)
    pag.click()
    pag.moveTo(308, 150)
    pag.click()
    pag.moveTo(168, 454)
    pag.click()


def open_cmd(x):
    pag.press('win')
    pag.write('cmd')
    pag.press('enter')
    s(0.5)
    pag.write(x)
    pag.press('enter')


r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=0.2)
    speak_text("How can I help you?")
    print('listening.....')
    audio = r.listen(source)
    user_input = [r.recognize_google(audio)]

command = convert(user_input)
