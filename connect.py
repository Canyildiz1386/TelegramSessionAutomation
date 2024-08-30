import os

# Set the path to ADB
adb_path = r"C:\platform-tools\adb.exe"

def adb_command(command):
    return os.system(f'"{adb_path}" {command}')

def get_connected_devices():
    try:
        result = os.popen(f'"{adb_path}" devices').read().strip().splitlines()
        if len(result) > 1:
            devices = [line.split()[0] for line in result[1:] if "device" in line]
            if devices:
                print(f"✅ {len(devices)} device(s) connected: {', '.join(devices)}")
            else:
                print("❌ No active devices found.")
        else:
            print("❌ No devices found.")
    except Exception as e:
        print(f"❌ An error occurred while getting the list of devices: {e}")

def connect_to_device(device_id):
    try:
        result = adb_command(f"connect {device_id}")
        if result == 0:
            print(f"✅ Connected to {device_id} successfully!")
        else:
            print(f"❌ Failed to connect to {device_id}.")
    except Exception as e:
        print(f"❌ An error occurred while connecting to {device_id}: {e}")

get_connected_devices()
connect_to_device("emulator-5554")
