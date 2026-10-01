from Xlib import X, XK
from Xlib.display import Display
from pynput.keyboard import Listener

display = Display()

def keycode_to_keysym(keycode):
    return display.keycode_to_keysym(keycode, 0)

def on_press(key):
    vk = getattr(key, "vk", None)
    if vk is None:
        return
    keysym = keycode_to_keysym(vk)
    char = XK.keysym_to_string(keysym)
    print("resolved:", repr(char))

with Listener(on_press=on_press) as listener:
    listener.join()