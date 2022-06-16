import eel
import keyboard
import peewee
import threading

from model import Script, Settings


RUN = False
eel.init('../front')

def puf_tab():
    keyboard.send('w')
    keyboard.send('tab')

def grid_tab():
    keyboard.send('o')
    keyboard.send('tab')

def combo():
    global RUN
    while RUN == True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'f' or event.name == 'F':
            keyboard.send('p')
            for i in range(4):
                puf_tab()
            keyboard.send('capslock')
            keyboard.send('2')

        if event.event_type == keyboard.KEY_DOWN and event.name == 'q' or event.name == 'Q':
            grid_tab()

@eel.expose
def set_key():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            print(event.name)
            return event.name


@eel.expose
def get_key(keys):
    print('я тут')
    print(keys)
    

@eel.expose
def activate(value):
    global RUN
    print(f'Скрипт - {value}')
    RUN = value
    if RUN == True:
        threading.Thread(target = combo).start()


def start():
    eel.start(
        'templates/index.html',
        jinja_templates='templates',
        mode="chrome",
        size=(650, 760)
    )

if __name__ == "__main__":
    start()