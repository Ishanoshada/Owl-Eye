from colorama import Fore, Back, Style
import pyfiglet
import requests
from bs4 import BeautifulSoup
import time
from .banner import display_banner
from .utils import check_network
from .whois_lookup import fetch_whois_data, extract_topics, extract_details

def display_custom_banner():
    banner =  """                                                                                
                                                                                
                         #                                                      
                        @.                                                      
                       &@  *                                                    

                       @&  ,@@@@@@@@@@@@@@@/.                                   
                      (@@    &@@@@@@@@@@@%*@@@@@@@.                             
                 @@&&&@@@%     *@@@@@@@@( ,@@@@@@@@@@@.                         

                                  .@@*&@%  & .@@@@@@@@@@@                       

                              ,       .@,*@&  @@@@@@@@@@@@@                     

                                @.          &@,@@@@@@@@@@@@@@                   

                               %@@@@*         @@@@@@@@@@@@@@@@/                 


                             &@ ,.,@@@@,       /@@@@@@@@@@@@@@@#                

                            @   #@@@@#(@@/      /%@@@@@@@@@@@@@@,               

                           %   #@@@.,,**#@@      @ @@@@@@@@@@@@@@               

                               %@@/.***/ .@@..   * /*@@@@@@@@@@@@,              

                               &@@# ,**/(%%&@&      .#@@@@@@@@@@@(              

                            ,  .@@@&.,****(#@@#     *&*@@@@@@@@@@/              

                             #.  @&@@@&*..(#@@%      @@@@@@@@@@@@.              

                               @.  &.#@@@@@@@@@,. . .&@@@@@@@@@@@               

                                  %%        *@&@@@@@@@@@@@@@@@@@                

                                                  @@@@@@@@@@@@@               

                                                   (@@@@@@@@@&                  

                                          **        @@@@@@@@                    

                                       #&@@* ./    #@@@@@@                      

                                     #.@@@@@@@@  .@@@@@(                        

                                   . @@@@@@@@%@@@@@@,                           

                                 @*@@ @@@@@@@@@*                                

                               .@@"""
    result = pyfiglet.figlet_format("               O w l  E y e")
    print(Fore.GREEN + banner)
    time.sleep(3)
    print(Fore.RED + result)
    time.sleep(3)
    print(Fore.YELLOW + "         [+]Coded By Black Owl[+]")
    time.sleep(3)
    print(Fore.YELLOW + "         [+]V0.1[+]\n\n")

def main():
    # Display the custom banner
    display_custom_banner()

    # Check network connectivity
    if not check_network():
        print(Fore.RED + "[+]No internet connection.... connect to internet & try again...")
        return

    # Get input from the user
    domain_or_ip = input("Enter Website URL or IP Address: ")

    # Fetch WHOIS data
    soup = fetch_whois_data(domain_or_ip)
    if not soup:
        return

    # Extract and display WHOIS data
    print("\nWHOIS Information:\n")
    try:
        # Display topics and details (example order)
        extract_topics(soup, 0)  # Topic 1
        extract_details(soup, 0)  # Example details
        extract_details(soup, 1)
        extract_details(soup, 2)
        extract_details(soup, 3)
    except Exception as e:
        print(Fore.RED + f"Error extracting data: {e}")

if __name__ == "__main__":
    main()
