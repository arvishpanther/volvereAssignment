import subprocess
import platform
import socket
import psutil
import uuid

def print_assignment_header():
    print("Volvere Assignment by Arvishpanther")
    print("=" * 40)

def get_installed_applications():
    try:
        command = 'Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Format-Table -AutoSize'
        result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True, check=True)

        print("\nInstalled Applications:")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error getting installed applications: {e}")

def get_internet_speed():
    try:
        command = 'speedtest-cli --simple'
        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)

        print("\nInternet Speed:")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error getting internet speed: {e}")

def get_screen_resolution():
    try:
        command = 'wmic desktopmonitor get screenheight, screenwidth'
        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)

        print("\nScreen Resolution:")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error getting screen resolution: {e}")

def get_cpu_info():
    print("\nCPU Model:")
    print(platform.processor())

    print("\nCPU Cores and Threads:")
    print(f"Physical Cores: {psutil.cpu_count(logical=False)}")
    print(f"Total Cores: {psutil.cpu_count(logical=True)}")

def get_gpu_info():
    try:
        command = 'wmic path win32_videocontroller get caption'
        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)

        print("\nGPU Model:")
        print(result.stdout.strip())

    except subprocess.CalledProcessError as e:
        print(f"Error getting GPU information: {e}")

def get_ram_size():
    print("\nRAM Size:")
    print(f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB")

def get_screen_size():
    try:
        command = 'wmic desktopmonitor get screensize'
        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)

        print("\nScreen Size:")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error getting screen size: {e}")

def get_public_ip():
    try:
        public_ip = socket.gethostbyname(socket.gethostname())
        print("\nPublic IP Address:")
        print(public_ip)

    except socket.error as e:
        print(f"Error getting public IP address: {e}")

def get_windows_version():
    print("\nWindows Version:")
    print(platform.version())


def get_mac_address(interface):
    try:
        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
        return mac

    except Exception as e:
        print(f"Error getting MAC address for {interface}: {e}")
        return None
if __name__ == "__main__":
    print_assignment_header()
    get_installed_applications()
    get_internet_speed()
    get_screen_resolution()
    get_cpu_info()
    get_gpu_info()
    get_ram_size()
    get_screen_size()
    get_public_ip()
    wifi_mac = get_mac_address("Wi-Fi")
    ethernet_mac = get_mac_address("Ethernet")
    if wifi_mac:
        print(f"Wi-Fi MAC Address: {wifi_mac}")
    if ethernet_mac:
        print(f"Ethernet MAC Address: {ethernet_mac}")
    get_windows_version()