import tkinter as tk
from time import sleep
import keyboard as kb
import pyautogui as pg
from pynput.keyboard import Listener
from pynput import keyboard

while True:
     pesca = pg.locateOnScreen('peixeverde.png', confidence=0.75)
     if pesca != None:
        vara = pg.locateOnScreen('varadepesca.png', confidence=0.75)
        x_vara, y_vara = pg.center(vara)
        pg.moveTo(x_vara, y_vara, 1)
        pg.click()