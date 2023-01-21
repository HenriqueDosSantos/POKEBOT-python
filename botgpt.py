import tkinter as tk
from time import sleep
import keyboard as kb
import pyautogui as pg
from pynput.keyboard import Listener
from pynput import keyboard

def update_coordinates(text):
    global POKE_POSITION, POKE_POSITION2, POKE_ENEMY, POKE_DEATH, DROP, LIST_ATACKS
    coordinates = text.split(',')
    POKE_POSITION = int(coordinates[0]), int(coordinates[1])
    POKE_POSITION2 = int(coordinates[2]), int(coordinates[3])
    POKE_ENEMY = int(coordinates[4]), int(coordinates[5])
    POKE_DEATH = int(coordinates[6]), int(coordinates[7])
    DROP = int(coordinates[8]), int(coordinates[9])
    LIST_ATACKS = coordinates[10:]
    
def poke():
    my_position = pg.position()
    pg.moveTo(POKE_POSITION)
    pg.click(button="right")
    pg.moveTo(my_position)
    
def poke2():
    my_position = pg.position()
    pg.moveTo(POKE_POSITION2)
    pg.click(button="right")
    pg.moveTo(my_position)
    
def poke_villan():
    my_position = pg.position()
    pg.moveTo(POKE_ENEMY)
    pg.click(button="left")
    pg.moveTo(my_position)

def loot():
    my_position = pg.position()
    pg.moveTo(POKE_DEATH)
    pg.click(button="right")
    pg.moveTo(DROP)
    pg.click(button="right")
    pg.click(button="right")
    pg.moveTo(my_position)

def atack(hotkey, delay=0.01):
    for item in hotkey:
        kb.press(item, delay)   
    
def key_code(key):
    if key == keyboard.Key.esc:
        return False
    if key == keyboard.Key.page_up:
        poke()
    if key == keyboard.Key.page_down:
        poke2()
    if key == keyboard.Key.space:
        poke_villan()
    if key == keyboard.Key.delete:
        loot()
    if key == keyboard.Key.space:
        atack(LIST_ATACKS)

def on_submit():
    update_coordinates(entry.get())

POKE_POSITION = 27, 535
POKE_POSITION2 = 79, 595
POKE_ENEMY = 343, 338
POKE_DEATH = 965, 530
DROP = 1696, 359
LIST_ATACKS = ['F1', 'F2', 'F3', 'F4', 'F5']

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

label = tk.Label(root, text="Digite as coordenadas no formato x1,y1,x2,y2")