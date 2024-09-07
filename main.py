import subprocess
import time

adb_path = r'C:\platform-tools\adb.exe'

def log(message, emoji="ℹ️"):
    print(f"{emoji} {message}")

def get_adb_devices():
    log("Checking for connected devices...", "🔌")
    result = subprocess.run([adb_path, 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = result.stdout
    devices = output.splitlines()[1:]
    devices = [line for line in devices if line.strip()]
    return devices

def connect_to_device(ip="127.0.0.1:5555"):
    log(f"Connecting to device {ip}...", "📡")
    result = subprocess.run([adb_path, 'connect', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if 'connected' in result.stdout:
        log(f"Successfully connected to {ip}", "✅")
    else:
        log(f"Failed to connect to {ip}: {result.stdout}", "❌")

def is_app_installed(package_name="de.mobileconcepts.cyberghost"):
    log(f"Checking if {package_name} is installed...", "🔍")
    result = subprocess.run([adb_path, 'shell', 'pm', 'list', 'packages'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if package_name in result.stdout:
        log(f"{package_name} is installed", "✅")
        return True
    else:
        log(f"{package_name} is not installed", "❌")
        return False

def close_cyberghost():
    log("Closing CyberGhost if it is running...", "🛑")
    subprocess.run([adb_path, '-s', '127.0.0.1:5555', 'shell', 'am', 'force-stop', 'de.mobileconcepts.cyberghost'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def open_cyberghost_on_bluestacks():
    log("Launching CyberGhost on BlueStacks...", "🚀")
    close_cyberghost()  # Close any running instance first
    subprocess.run([adb_path, '-s', '127.0.0.1:5555', 'shell', 'monkey', '-p', 'de.mobileconcepts.cyberghost -c android.intent.category.LAUNCHER 1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if check_for_label('Agree &'):
        click_on_bluestacks(465, 727)
        log("Clicked 'Agree &'", "✅")
        time.sleep(20)

    time.sleep(30)
    if check_for_label('Existing'):
        click_on_bluestacks(237, 737)
        log("Clicked 'Existing user?'", "✅")
    
    if check_for_label('Login'):
        click_on_bluestacks(246, 346)
        log("Clicked 'Login'", "✅")
        input_text_on_bluestacks('kelly_yen@hotmail.com')
        log("Entered email", "✉️")
        click_on_bluestacks(250, 429)
        input_text_on_bluestacks('2Agujjlu!')
        log("Entered password", "🔑")
        click_on_bluestacks(285, 504)
        time.sleep(40)

    if check_for_label('OK'):
        click_on_bluestacks(283, 611)
        click_on_bluestacks(426, 593)
        log("Clicked 'OK' and proceeded", "✅")
        time.sleep(40)
        click_on_bluestacks(296, 364)
        click_on_bluestacks(432, 524)
    
    if check_for_label("Connect to"):
        click_on_bluestacks(282, 442)
        log("Clicked 'Connect to'", "✅")
        time.sleep(30)
        click_on_bluestacks(503, 54)
        input_text_on_bluestacks('France')
        log("Selected 'France' location", "🌍")
        click_on_bluestacks(177, 227)
        time.sleep(40)
        log("Connected to France", "🔒")

def check_for_label(label):
    ui_content = get_ui_hierarchy()
    if ui_content and label in ui_content:
        log(f"Label '{label}' found!", "🔍")
        return True
    else:
        log(f"Label '{label}' not found.", "❌")
        return False

def click_on_bluestacks(x, y):
    log(f"Clicking at position ({x}, {y})", "🖱️")
    subprocess.run([adb_path, '-s', '127.0.0.1:5555', 'shell', 'input', 'tap', str(x), str(y)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def input_text_on_bluestacks(text):
    log(f"Inputting text: {text}", "⌨️")
    subprocess.run([adb_path, '-s', '127.0.0.1:5555', 'shell', 'input', 'text', text], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def get_ui_hierarchy():
    log("Dumping UI hierarchy...", "📄")
    subprocess.run([adb_path, '-s', '127.0.0.1:5555', 'shell', 'uiautomator', 'dump', '/sdcard/ui.xml'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    subprocess.run([adb_path, '-s', '127.0.0.1:5555', 'pull', '/sdcard/ui.xml', './ui.xml'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    try:
        with open('ui.xml', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        log("UI dump file not found.", "❌")
        return None

if __name__ == "__main__":
    devices = get_adb_devices()
    if devices:
        for device in devices:
            log(f"Device found: {device}", "📱")
    else:
        log("No devices connected.", "❌")

    connect_to_device()


    open_cyberghost_on_bluestacks()
