import requests
import re

# Function to initiate a session and fetch the initial page
def start_session(domain):
    session = requests.Session()

    # Send initial GET request to obtain cookies
    initial_url = "https://www.namecheap.com/domains/whois/"
    response = session.get(initial_url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
    })

    if response.status_code == 200:
        #print("Initial GET request successful. Cookies set.")
        return session, domain
    else:
        print(f"Error with initial request: {response.status_code}")
        return None, None

# Function to fetch the WHOIS data with the session and set cookies
def fetch_whois_data(session, domain):
    url = f"https://www.namecheap.com/domains/contactlookup-api/whois/lookupraw/{domain}"

    response = session.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
    })

    if response.status_code == 200:
        return response.text  # Return raw WHOIS text data
    else:
        print(f"Error fetching WHOIS data: {response.status_code}")
        return None

import re
from datetime import datetime
from typing import Dict, Any

def parse_whois_response(whois_data: str) -> Dict[str, Any]:
    """
    Parse raw WHOIS response data into a structured dictionary.
    
    Args:
        whois_data (str): Raw WHOIS response text
        
    Returns:
        Dict[str, Any]: Structured WHOIS data
    """
    # Clean the input data
    whois_data = whois_data.strip()
    
    # Define patterns for all relevant fields
    patterns = {
        'domain_name': r'Domain Name:\s*(\S+)',
        'registry_domain_id': r'Registry Domain ID:\s*(\S+)',
        'registrar_whois_server': r'Registrar WHOIS Server:\s*(\S+)',
        'registrar_url': r'Registrar URL:\s*(\S+)',
        'updated_date': r'Updated Date:\s*(\S+)',
        'creation_date': r'Creation Date:\s*(\S+)',
        'expiry_date': r'Registry Expiry Date:\s*(\S+)',
        'registrar': r'Registrar:\s*(\d+)',
        'registrar_iana_id': r'Registrar IANA ID:\s*(\d+)',
        'registrar_abuse_email': r'Registrar Abuse Contact Email:\s*(\S+)',
        'registrar_abuse_phone': r'Registrar Abuse Contact Phone:\s*(\S+)',
       
        'nameservers': r'Name Server:\s*(\S+)',
        'dnssec': r'DNSSEC:\s*(\S+)',
        
    }
    
    # Initialize results dictionary
    parsed_data = {}
    
    # Extract data for each field
    for key, pattern in patterns.items():
        matches = re.findall(pattern, whois_data, re.IGNORECASE)
        if matches:
            if key == 'nameservers':
                parsed_data[key] = matches  # Keep all nameservers
            else:
                parsed_data[key] = matches[0].strip()
        else:
            parsed_data[key] = None
            
    # Convert dates to datetime objects where applicable
    date_fields = ['updated_date', 'creation_date', 'expiry_date', 'last_update']
    for field in date_fields:
        if parsed_data.get(field):
            try:
                # Handle the timezone format in the dates
                date_str = parsed_data[field].replace('Z', '+00:00')
                parsed_data[field] = datetime.fromisoformat(date_str)
            except ValueError:
                # Keep original string if parsing fails
                pass
    
    return parsed_data
def print_parsed_data(parsed_data: Dict[str, Any]) -> None:
        """
        Print parsed WHOIS data in a formatted way.
        
        Args:
            parsed_data (Dict[str, Any]): Parsed WHOIS data
        """
        # Define display names for better readability
        display_names = {
            'domain_name': 'Domain Name',
            'registry_domain_id': 'Registry Domain ID',
            'registrar_whois_server': 'Registrar WHOIS Server',
            'registrar_url': 'Registrar URL',
            'updated_date': 'Updated Date',
            'creation_date': 'Creation Date',
            'expiry_date': 'Expiry Date',
            'registrar': 'Registrar',
            'registrar_iana_id': 'Registrar IANA ID',
            'registrar_abuse_email': 'Registrar Abuse Email',
            'registrar_abuse_phone': 'Registrar Abuse Phone',
            'domain_status': 'Domain Status',
            'nameservers': 'Name Servers',
            'dnssec': 'DNSSEC',
            'last_update': 'Last Update'
        }
        
        # Print each field
        for key, display_name in display_names.items():
            value = parsed_data.get(key)
            
            if value is not None:
                if isinstance(value, list):
                    print(f"\t{display_name}:")
                    for item in value:
                        print(f"\t  - {str(item.strip()).split('\\r')[0]}")
                else:
                    print(f"\t{display_name}: {str(value).split('\\r')[0]}")

def get_data(domain):
    session, domain = start_session(domain)

    if session and domain:
        whois_data = fetch_whois_data(session, domain)
        whois_data 
        if whois_data:
            parsed_data = parse_whois_response(whois_data)
            print_parsed_data(parsed_data)
