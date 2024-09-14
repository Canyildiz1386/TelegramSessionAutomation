import subprocess
import time
import speech_recognition as sr
from datetime import datetime
import os

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

def close_app(package_name):
    log(f"Closing {package_name} if it is running...", "🛑")
    subprocess.run([adb_path, '-s', '127.0.0.1:5555', 'shell', 'am', 'force-stop', package_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def open_app_on_bluestacks(package_name, start_label=None):
    log(f"Launching {package_name} on BlueStacks...", "🚀")
    close_app(package_name)
    subprocess.run([adb_path, '-s', '127.0.0.1:5555', 'shell', 'monkey', '-p', package_name, '-c', 'android.intent.category.LAUNCHER', '1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    time.sleep(2)
    if start_label and check_for_label(start_label):
        click_on_bluestacks(398, 463)
        log(f"Clicked '{start_label}'", "✅")
        time.sleep(3)

def open_cyberghost_on_bluestacks():
    open_app_on_bluestacks('de.mobileconcepts.cyberghost', 'Agree &')
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
        click_on_bluestacks(433, 591)
    
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

def open_telegram_on_bluestacks():
    open_app_on_bluestacks('org.telegram.messenger')
    if check_for_label('My Story'):
        click_on_bluestacks(30,46)
        time.sleep(1)
        click_on_bluestacks(176,198)
        time.sleep(1)

        click_on_bluestacks(166,350)
        time.sleep(1)

        click_on_bluestacks(71,465)
        time.sleep(1)
 

def open_efon_on_bluestacks():

    open_app_on_bluestacks('io.efon', 'Start')
    time.sleep(1)


    input_text_on_bluestacks('+43650110000')
    click_on_bluestacks(266,851)
    time.sleep(2)
    phone_number = '6505012991'
    number_to_coordinates = {
        '0': (272, 781),
        '1': (157, 376),
        '2': (278, 377),
        '3': (388, 360),
        '4': (149, 525),
        '5': (290, 514),
        '6': (398, 516),
        '7': (153, 652),
        '8': (266, 647),
        '9': (390, 648),
        '*' : (162,780),
        '#' : (395,783)
        
    }
    time.sleep(7)
    click_on_bluestacks(39,176)
    time.sleep(2)
    click_on_bluestacks(420,922)
    for digit in phone_number:
        if digit in number_to_coordinates:
            x, y = number_to_coordinates[digit]
            click_on_bluestacks(x, y)
            log(f"Tapped on digit {digit} at ({x}, {y})", "🖱️")
            time.sleep(1) 
    click_on_bluestacks(395,783)
    time.sleep(5)
    click_on_bluestacks(440,198)
    click_on_bluestacks(119,923)
    time.sleep(3)
    click_on_bluestacks(287,564)


def get_latest_file_in_directory(directory):
    log(f"Finding the latest file in {directory}...", "🔍")
    result = subprocess.run([adb_path, 'shell', f'ls -t {directory}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    files = result.stdout.splitlines()
    if files:
        latest_file = files[0].strip()
        log(f"Latest file found: {latest_file}", "✅")
        return latest_file
    else:
        log("No files found in the directory.", "❌")
        return None

def pull_audio_file():
    directory = '/storage/emulated/0/Android/data/io.efon/files/Download/'
    latest_file = get_latest_file_in_directory(directory)
    if latest_file:
        local_path = os.path.join(os.getcwd(), 'efon_audio_recording.mp3')
        adb_remote_path = os.path.join(directory, latest_file)
        subprocess.run([adb_path, 'pull', adb_remote_path, local_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if os.path.exists(local_path):
            log(f"Audio file pulled successfully to {local_path}", "✅")
            return local_path
        else:
            log("Failed to pull audio file.", "❌")
            return None
    else:
        return None
    

def convert_mp3_to_wav(mp3_file):
    wav_file = os.path.splitext(mp3_file)[0] + '.wav'
    log(f"Converting {mp3_file} to {wav_file}...", "🔄")
    result = subprocess.run(['ffmpeg', '-i', mp3_file, wav_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        log(f"Conversion successful: {wav_file}", "✅")
        return wav_file
    else:
        log(f"Failed to convert {mp3_file} to WAV.", "❌")
        return None

def convert_audio_to_text(audio_file_path):
    log(f"Converting {audio_file_path} to text...", "📝")
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        log(f"Conversion complete: {text}", "✅")
        return text
    except sr.UnknownValueError:
        log("Google Speech Recognition could not understand the audio.", "❌")
    except sr.RequestError as e:
        log(f"Could not request results from Google Speech Recognition service; {e}", "❌")
    return None

if __name__ == "__main__":
    devices = get_adb_devices()
    if devices:
        for device in devices:
            log(f"Device found: {device}", "📱")
    else:
        log("No devices connected.", "❌")

    # open_efon_on_bluestacks()

    # mp3_audio_file = pull_audio_file()
    # if mp3_audio_file:
    #     wav_audio_file = convert_mp3_to_wav(mp3_audio_file)
    #     if wav_audio_file:
    #         text_output = convert_audio_to_text(wav_audio_file)
    #         if text_output:
    #             log(f"Transcribed Text: {text_output}", "📝")

    
    open_telegram_on_bluestacks()