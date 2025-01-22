from colorama import Fore
from bs4 import BeautifulSoup
import requests

def fetch_whois_data(domain):
    try:
        page = requests.get(f"https://who.is/whois/{domain}")
        soup = BeautifulSoup(page.text, "html.parser")
        return soup
    except Exception as e:
        print(Fore.RED + f"Error fetching data: {e}")
        return None

def extract_topics(soup, index):
    try:
        topic = soup.find_all("span", class_="lead")[index]
        print(Fore.CYAN + f"~~ {topic.text} ~~\n\n")
    except IndexError:
        print(Fore.RED + "Topic index out of range.")

def extract_details(soup, index):
    try:
        key = soup.find_all("div", class_="col-md-4 queryResponseBodyKey")[index].text
        value = soup.find_all("div", class_="col-md-8 queryResponseBodyValue")[index].text
        print(Fore.YELLOW + f">> {key} = {value}\n")
    except IndexError:
        print(Fore.RED + "Detail index out of range.")
