from colorama import Fore, Back, Style
import pyfiglet
import time
from .banner import display_banner
from .utils import check_network
from .whois_lookup import start_session, fetch_whois_data, parse_whois_response, print_parsed_data

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
    time.sleep(2)
    print(Fore.RED + result)
    time.sleep(2)
    print(Fore.YELLOW + "         [+]Coded By Black Owl[+]")
    time.sleep(1)
    print(Fore.YELLOW + "         [+]V0.1.1[+]\n\n")

def main():
    # Display the custom banner
    display_custom_banner()

    # Check network connectivity
    if not check_network():
        print(Fore.RED + "[+]No internet connection.... connect to internet & try again...")
        return

    # Get input from the user
    domain = input("Enter Website URL or IP Address: ")


    # Extract and display WHOIS data
    print("\nWHOIS Information:\n")
    try:
        session, domain = start_session(domain)

        if session and domain:
            whois_data = fetch_whois_data(session, domain)
            whois_data 
            if whois_data:
                parsed_data = parse_whois_response(whois_data)
                print_parsed_data(parsed_data)

        
    except Exception as e:
        print(Fore.RED + f"Error extracting data: {e}")

if __name__ == "__main__":
    main()
