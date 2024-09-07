import subprocess
import os
import time

adb_path = r'C:\platform-tools\adb.exe'

def get_adb_devices():
    result = subprocess.run([adb_path, 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = result.stdout
    devices = output.splitlines()[1:]
    devices = [line for line in devices if line.strip()]
    return devices

def connect_to_device(ip="127.0.0.1:5555"):
    result = subprocess.run([adb_path, 'connect', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if 'connected' in result.stdout:
        print(f"Successfully connected to {ip}")
    else:
        print(f"Failed to connect to {ip}: {result.stdout}")


def open_cyberghost_on_bluestacks():
    subprocess.run([adb_path, '-s', '127.0.0.1:5555', 'shell', 'monkey', '-p', 'de.mobileconcepts.cyberghost -c android.intent.category.LAUNCHER 1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if check_for_button('Agree') :
        click_on_bluestacks(692,1283)
        time.sleep(20)
    time.sleep(10)
    if check_for_button('Existing user?'):
        click_on_bluestacks(448,1390)
    
    if check_for_button('Login'):
        click_on_bluestacks(396,524)

        input_text_on_bluestacks(
            'kelly_yen@hotmail.com'
        )
        click_on_bluestacks(337,693)
        input_text_on_bluestacks(
            '2Agujjlu!'
        )
        click_on_bluestacks(512,842)
    time.sleep(10)

    if check_for_button('OK'):
        click_on_bluestacks(401,1033)
    return

    

    time.sleep(5)
    click_on_bluestacks(529,1021)


def check_for_button(text):
    ui_content = get_ui_hierarchy()
    if ui_content and text in ui_content:
        print(f"Button with text '{text}' found!")
        return True
    else:
        print(f"Button with text '{text}' not found.")
        return False

def click_on_bluestacks(x, y):
    subprocess.run([adb_path, '-s', '127.0.0.1:5555', 'shell', 'input', 'tap', str(x), str(y)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
def input_text_on_bluestacks(text):
    subprocess.run([adb_path, '-s', '127.0.0.1:5555', 'shell', 'input', 'text', text], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def get_ui_hierarchy():
    # Dump UI hierarchy to a file
    subprocess.run([adb_path, '-s', '127.0.0.1:5555', 'shell', 'uiautomator', 'dump', '/sdcard/ui.xml'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Pull the file to the local machine
    subprocess.run([adb_path, '-s', '127.0.0.1:5555', 'pull', '/sdcard/ui.xml', './ui.xml'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Read the contents of the dumped XML file
    try:
        with open('ui.xml', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("UI dump file not found.")
        return None
if __name__ == "__main__":
    devices = get_adb_devices()
    if devices:
        for device in devices:
            print(device)
    else:
        print("No devices connected.")

    connect_to_device()

    open_cyberghost_on_bluestacks()

