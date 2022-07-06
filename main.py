import eel
import keyboard
import threading

RUN = False
eel.init('front')

def sstr(ch):
    if ch == '':
        return '-'
    else:
        return str(ch)

def write_key(list):
    with open('key.txt','w+') as doc:
        for key in list:
            doc.write(sstr(key) + ' ')
        doc.close()

def read_key():
    with open('key.txt','r') as doc:
        data = doc.read()
        lst = data.split(' ')
        
        return lst

def puf_tab():
    keyboard.send('w')
    keyboard.send('tab')

def grid_tab():
    keyboard.send('o')
    keyboard.send('tab')

def combo():
    global RUN
    keys = read_key()
    for key in keys:
        print(key)
    while RUN == True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == keys[2] or event.name == keys[2].upper():
            keyboard.send('p')
            for i in range(4):
                puf_tab()
            keyboard.send('capslock')
            keyboard.send('2')

        if event.event_type == keyboard.KEY_DOWN and event.name == keys[0] or event.name == keys[0].upper():
            grid_tab()

        if event.event_type == keyboard.KEY_DOWN and event.name == keys[1] or event.name == keys[1].upper():
            for i in range(5):
                puf_tab()

@eel.expose
def set_key(keys):
    write_key(keys)

@eel.expose
def get_key(id):
    lst = read_key()
    return(str(lst[int(id)]))

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