import subprocess
import requests

# Function to get the IP address of the device
def get_ip():
    ip_output = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
    ip_address = ip_output.stdout.strip()
    return ip_address

# Function to search for available Wi-Fi networks
def search_wifi():
    output = subprocess.run(['nmcli', '-t', 'device', 'wifi', 'list'], capture_output=True, text=True)
    lines = output.stdout.splitlines()
    networks = [(index, line.split(':')[7]) for index, line in enumerate(lines)]
    return networks

# Function to check if the entered SSID is valid and returns the index and SSID
def check_ssid(ssid, networks):
    if ssid.isdigit():  # If a number is entered as SSID
        index = int(ssid)
        ssid = networks[index][1]
    else:  # If a string is entered as SSID
        for network in networks:
            if ssid == network[1]:
                index = network[0]
                break
        else:  # If the SSID is not found in the list
            print("SSID not found in the list.")
            return None
    return (index, ssid)

# Function to connect to the specified Wi-Fi network
def connect_wifi(ssid, passwd):
    subprocess.run(['nmcli', 'device', 'wifi', 'connect', ssid, 'password', passwd], capture_output=True, text=True)

# Get the initial IP address
num_ip_first = get_ip()

# Search for available Wi-Fi networks
networks = search_wifi()
print('Available networks:')
for index, network in networks:
    print(f"{index} : {network}")

# Get SSID and password From User
ssid = input('Enter the SSID OR NUMID: ')
passwd = input('Enter the password: ')

# Check if the entered SSID is valid and get its index and SSID
ssid_index = check_ssid(ssid, networks)
if ssid_index is not None:
    # Connect to the specified Wi-Fi network
    connect_wifi(ssid_index[1], passwd)
    # Get the current IP address after connecting to the network
    num_ip_end = get_ip()

    # Check if the IP address has changed after connecting
    if num_ip_end != num_ip_first:
        print(f'You Connected Got Another IP : {num_ip_end}')
    else:
        print('You Not Connected!!!')

# Check internet connection Function
def check_internet():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
        return False
    except requests.Timeout:
        print("Timeout occurred while trying to connect.")
        return False
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Check internet connection status and print the result
if check_internet():
    print("Internet connection is active.")
else:
    print("No internet connection.")
