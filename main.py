import os
import time

def adb_command(command):
    result = os.system(f"adb shell {command}")
    if result == 0:
        print(f"✅ Command '{command}' executed successfully!")
    else:
        print(f"❌ Command '{command}' failed to execute.")

def tap(x, y):
    adb_command(f"input tap {x} {y}")

def input_text(text):
    result = os.system(f'adb shell input text "{text}"')
    if result == 0:
        print(f"✅ Text '{text}' entered successfully!")
    else:
        print(f"❌ Failed to enter text '{text}'.")

def key_event(key):
    result = os.system(f"adb shell input keyevent {key}")
    if result == 0:
        print(f"✅ Key event '{key}' executed successfully!")
    else:
        print(f"❌ Key event '{key}' failed to execute.")

try:
    result = os.system("adb connect localhost:5555")
    if result == 0:
        print("✅ Connected to BlueStacks successfully!")
    else:
        print("❌ Failed to connect to BlueStacks.")

    result = os.system("adb push /path/to/your/tdata /storage/emulated/0/Android/data/org.telegram.messenger/files/")
    if result == 0:
        print("✅ tdata folder pushed successfully!")
    else:
        print("❌ Failed to push tdata folder.")

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
    
    print("✅ Phone number change process completed successfully!")
except Exception as e:
    print(f"❌ An error occurred: {e}")
