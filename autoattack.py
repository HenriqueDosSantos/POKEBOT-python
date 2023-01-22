import bt
import keyboard as kb
import tkinter as tk
import pyautogui as pg
import PySimpleGUI as sg
from pynput.keyboard import Listener
from pynput import keyboard
from time import sleep

sg.theme('Reds')
layout = [  
        [sg.Text('Seja bem vindo ao POkebot logo abaixo você verá os comandos disponivel no momento')],
        [sg.Text("\nPage_up = invocar pokemon 1\nPage_down = invoca pokemon 2\nBackspace = mira no pokemon\nBackspace = usa os moveatack do pokemon\nDelete = coleta os drop do pokemon\nESC = encerra o programa")],
        [sg.Button('OK')]
        ]
window = sg.Window('POKEBOT', layout)
POKE_POSITION = 27, 535
POKE_POSITION2 = 79, 595
POKE_ENEMY = 343, 338
POKE_DEATH = 965, 530
DROP = 1696, 359
LIST_ATACKS = ['F1', 'F2', 'F3', 'F4', 'F5']

while True:
    event, values = window.read()
    if event in ('OK'):
        break
    print('You entered ', values[0])
    
window.close()

while True:
    PESCA = pg.locateOnScreen("peixeverde.png", confidence=0.80)
    if PESCA != None:
        VARA = pg.locateOnScreen("varadepesca.png", confidence=0.80)

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
        kb.press(bt.key[item], delay)   
    
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
    
with Listener(on_press=key_code) as listener:
    listener.join()
    