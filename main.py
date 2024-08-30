import os
import time

def adb_command(command):
    os.system(f"adb shell {command}")

def tap(x, y):
    adb_command(f"input tap {x} {y}")

def input_text(text):
    adb_command(f"input text {text}")

def key_event(key):
    adb_command(f"input keyevent {key}")

os.system("adb connect localhost:5555")
os.system("adb push /path/to/your/tdata /storage/emulated/0/Android/data/org.telegram.messenger/files/")
adb_command("monkey -p org.telegram.messenger -c android.intent.category.LAUNCHER 1")
time.sleep(10)
tap(100, 100)
time.sleep(2)
tap(200, 400)
time.sleep(2)
tap(300, 500)
time.sleep(2)
tap(300, 600)

new_phone_number = "1234567890"
input_text(new_phone_number)
key_event(66)
time.sleep(2)
tap(400, 700)
