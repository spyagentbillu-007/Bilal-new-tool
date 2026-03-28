# MR.BILAL Ultra WiFi Scanner - PRO Final
# Fully upgraded version with real useful tools
# Requires: termux-api, python installed

import os
import time
import json
import datetime

# Colors
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Banner with info lines
def banner():
    print(CYAN + r"""
███╗   ███╗██████╗ ██╗     ██████╗      ██████╗ ██╗██████╗ 
████╗ ████║██╔══██╗██║     ██╔══██╗    ██╔═══██╗██║██╔══██╗
██╔████╔██║██████╔╝██║     ██║  ██║    ██║   ██║██║██████╔╝
██║╚██╔╝██║██╔═══╝ ██║     ██║  ██║    ██║   ██║██║██╔═══╝ 
██║ ╚═╝ ██║██║     ███████╗██████╔╝    ╚██████╔╝██║██║     
╚═╝     ╚═╝╚═╝     ╚══════╝╚═════╝      ╚═════╝ ╚═╝╚═╝     
""" + RESET)
    print(GREEN + "1️⃣  GitHub: spyagentbillu_007" + RESET)
    print(YELLOW + "2️⃣  Author: Mr.BILAL | Programmer | Coding Expert | Developer" + RESET)
    print(RED + "3️⃣  Attitude: 💀 fucker 💀" + RESET)
    print(CYAN + "4️⃣  Khan khetY Hein 🌾" + RESET)
    print("\n" + CYAN + "🔹 Created by MR.BILAL 🔹\n" + RESET)

# Check Termux API
def check_termux_api():
    if os.system("command -v termux-wifi-scaninfo > /dev/null") != 0:
        print(RED + "\n⚠ Termux:API not found! Install it first:" + RESET)
        print("pkg install termux-api")
        return False
    return True

# Scan WiFi networks
def scan_wifi():
    print(CYAN + "\n🔍 Scanning WiFi networks...\n" + RESET)
    time.sleep(1)
    
    try:
        output = os.popen("termux-wifi-scaninfo").read()
        if not output.strip():
            print(RED + "⚠ No networks found. Make sure WiFi & Location are ON!" + RESET)
            return
        
        networks = json.loads(output)
        sorted_networks = sorted(networks, key=lambda x: x.get("level", 0), reverse=True)
        
        print("Top 5 Strongest Networks:")
        print("-" * 40)
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("wifi_log.txt", "a") as f:
            f.write(f"\nScan at {timestamp}\n")
        
        for idx, net in enumerate(sorted_networks[:5], 1):
            ssid = net.get("ssid", "Unknown")
            level = net.get("level", 0)
            flags = net.get("capabilities", "")
            open_status = "Open" if "WEP" not in flags and "WPA" not in flags else "Secured"
            
            # Color coding
            if level > -50:
                color = GREEN
                strength = "Strong"
            elif -70 <= level <= -50:
                color = YELLOW
                strength = "Medium"
            else:
                color = RED
                strength = "Weak"
            
            line = f"{idx}. {ssid} | Signal: {level} dBm | {strength} | {open_status}"
            print(color + line + RESET)
            
            with open("wifi_log.txt", "a") as f:
                f.write(line + "\n")
        
        # Internet check
        connected = os.popen("ping -c 1 8.8.8.8").read()
        if "1 packets transmitted, 1 received" in connected:
            print(GREEN + "\n✅ Internet is available." + RESET)
        else:
            print(YELLOW + "\n⚠ Internet may not be available." + RESET)
        
        print("\nScan complete! Results saved to wifi_log.txt\n")
    
    except Exception as e:
        print(RED + "❌ Error scanning WiFi:" + str(e) + RESET)

# Install all Termux packages
def install_termux_packages():
    print(CYAN + "\n⚡ Installing essential Termux packages...\n" + RESET)
    packages = ["python", "git", "curl", "wget", "nano", "vim", "termux-api", "openssh", "tsu", "clang", "nodejs"]
    for pkg in packages:
        print(YELLOW + f"Installing {pkg}..." + RESET)
        os.system(f"pkg install -y {pkg}")
    print(GREEN + "\n✅ All essential packages installed/updated!" + RESET)

# Main menu
def main():
    banner()
    if not check_termux_api():
        return
    
    while True:
        print(CYAN + "Menu:" + RESET)
        print("1. Scan WiFi (Top 5 + Open WiFi info)")
        print("2. Auto Scan Every 10s")
        print("3. Install All Essential Termux Packages")
        print("4. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            scan_wifi()
        elif choice == "2":
            print(CYAN + "\n🚀 Auto scanning started! Press CTRL+C to stop.\n" + RESET)
            try:
                while True:
                    scan_wifi()
                    print("Next scan in 10 seconds...\n")
                    time.sleep(10)
            except KeyboardInterrupt:
                print(YELLOW + "\nAuto scan stopped!" + RESET)
        elif choice == "3":
            install_termux_packages()
        elif choice == "4":
            print("\nExiting... Bye! 👋\n")
            print("🔹 Created by MR.BILAL 🔹")
            break
        else:
            print(RED + "❌ Invalid choice! Try again." + RESET)

if __name__ == "__main__":
    main()
