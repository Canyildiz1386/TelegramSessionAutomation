import subprocess
import time
import os
from pydub import AudioSegment
import speech_recognition as sr

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
    open_app_on_bluestacks('org.telegram.messenger', 'Start Messaging')
    time.sleep(3)
    click_on_bluestacks(638, 317)
    input_text_on_bluestacks('+14417043455')
    click_on_bluestacks(898, 483)
    time.sleep(3)
    click_on_bluestacks(902, 408)
    click_on_bluestacks(615, 396)
    time.sleep(1)
    click_on_bluestacks(641, 314)

def open_efon_on_bluestacks():
    start_audio_recording()
    open_app_on_bluestacks('io.efon', 'Start')
    time.sleep(1)
    input_text_on_bluestacks('+43650110000')
    click_on_bluestacks(266, 851)
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
    click_on_bluestacks(39, 176)
    time.sleep(2)
    click_on_bluestacks(420, 922)
    for digit in phone_number:
        if digit in number_to_coordinates:
            x, y = number_to_coordinates[digit]
            click_on_bluestacks(x, y)
            log(f"Tapped on digit {digit} at ({x}, {y})", "🖱️")
            time.sleep(1)
    click_on_bluestacks(395, 783)
    time.sleep(5)
    click_on_bluestacks(440, 198)
    click_on_bluestacks(119, 923)
    time.sleep(3)
    click_on_bluestacks(287, 564)

def start_audio_recording():
    global recording_process
    log("Starting audio recording in the background...", "🎙️")
    recording_process = subprocess.Popen([adb_path, '-s', '127.0.0.1:5555', 'shell', 'screenrecord', '--output-format=mp4', '/sdcard/audio_recording.mp4'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def stop_audio_recording():
    global recording_process
    log("Stopping audio recording...", "🛑")
    if recording_process:
        recording_process.terminate()
        recording_process = None
    project_path = os.path.dirname(os.path.realpath(__file__))
    local_recording_path = os.path.join(project_path, 'audio_recording.mp4')
    subprocess.run([adb_path, '-s', '127.0.0.1:5555', 'pull', '/sdcard/audio_recording.mp4', local_recording_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    log(f"Recording saved to {local_recording_path}", "✅")
    local_audio_path = os.path.join(project_path, 'audio_recording.wav')
    log("Extracting audio from video using pydub...", "🎧")
    audio = AudioSegment.from_file(local_recording_path, format="mp4")
    audio.export(local_audio_path, format="wav")
    log(f"Audio extracted and saved to {local_audio_path}", "✅")
    return local_audio_path

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
    connect_to_device()
    open_efon_on_bluestacks()
    audio_file_path = stop_audio_recording()
    if audio_file_path:
        text_output = convert_audio_to_text(audio_file_path)
        if text_output:
            log(f"Transcribed Text: {text_output}", "📝")
