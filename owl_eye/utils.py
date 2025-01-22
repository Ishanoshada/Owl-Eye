from colorama import Fore
import requests

def check_network():
    try:
        requests.get("https://www.google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        print(Fore.RED + "[+] No internet connection. Connect to the internet and try again.")
        return False
