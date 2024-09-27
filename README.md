WiFi-AutoConnect

WiFi-AutoConnect is a Python script that automates the process of searching for available Wi-Fi networks, connecting to them using SSID or network index, and verifying internet connectivity. This script is ideal for environments where manual connection to networks can be cumbersome or when automating Wi-Fi connections on a Linux machine.

Features

    . Fetches the current IP address before and after connecting to Wi-Fi.
    . Lists all available Wi-Fi networks using nmcli.
    . Allows users to connect to a Wi-Fi network by selecting either SSID or network index.
    . Verifies whether the IP address changes after connection.
    . Checks for active internet connection by pinging Google's servers.
    . Provides error handling for connection issues.

Requirements

    . Python 3.x
    . nmcli (installed by default on most Linux distributions)
    . requests library

Installation

    git clone https://github.com/yourusername/WiFi-AutoConnect.git
    cd WiFi-AutoConnect


Install required dependencies:


    pip install requests

Usage


    python3 wifi_autoconnect.py

    . The script will display all available Wi-Fi networks. You can choose a network by either:
        1. Entering the SSID of the network.
        2. Entering the index number associated with the network in the list.

    . You will be prompted to enter the Wi-Fi password.

    . Once connected, the script will:
        . Display your new IP address if the connection is successful.
        . Verify whether your internet connection is active by checking Google's servers.

Example:


       1. 
       $ python3 wifi_autoconnect.py
        
       2. 
        Available networks:
        0 : MyHomeWiFi
        1 : CoffeeShopWiFi
        2 : OfficeWiFi

        3.
        Enter the SSID OR NUMID: 1
        
        4.
        Enter the password: mysecretpassword
        You Connected Got Another IP: 192.168.0.100
        Internet connection is active.

Troubleshooting

    SSID Not Found: If the SSID is not found, ensure the network is available and try scanning again.
    Connection Issues: Make sure that the Wi-Fi password is correct. If the connection fails, it will display an error message.
    No Internet: If the script reports "No internet connection," verify that the Wi-Fi connection is successful and troubleshoot network settings if needed.
