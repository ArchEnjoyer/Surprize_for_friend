import keyboard
import time

def enter():
    keyboard.send("enter")
    time.sleep(0.6)

keyboard.send("windows")
time.sleep(0.3)
keyboard.write("блокнот")
time.sleep(0.3)
enter()
keyboard.write("""
С днём рождения, друганыч!

Тебе уже целых 18 годиков, вау, ты че такой старый?!

Ну желаем тебе всего самого-самого (желаем в смысле я с шизой), благ там, удачи

ТЫ ДЕЙСТВИТЕЛЬНО ЛУЧШИЙ ДРУГ С ДЕТСТВА ФОРЕВА

A____A
|・ㅅ・| Meow
|っ　ｃ|
|　　　|
|　　　|
|　　　|
|　　　|
|　　　|
|　　　| I Hope
|　　　| You have
|　　　| everything nice as ice! :3
 U￣￣U

""", delay=0.05)
