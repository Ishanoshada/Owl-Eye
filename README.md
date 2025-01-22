
# Owl-Eye

Owl-Eye is a Python package that allows users to perform WHOIS lookups for domains or IP addresses. It parses and displays essential information such as registration details, name servers, ownership details, and more.

This package is based on the original script by [LaviruD](https://github.com/LaviruD/Owl-Eye) and has been modularized and packaged for ease of use and distribution.

---

## Features
- Retrieve WHOIS information for any domain or IP address.
- Parse data such as:
  - Domain ownership.
  - Registration dates.
  - Name servers.
  - Administrative and technical contact details (if available).
- Simple command-line interface (CLI).
- Displays results in a well-organized format.

---

## Installation

Install Owl-Eye using pip:

```bash
pip install owl-eye
```

---

## Usage

### Command-Line Usage
After installation, you can use Owl-Eye directly from the terminal:

```bash
owl-eye
```

Follow the on-screen prompts to provide a domain or IP address for the WHOIS lookup.

---

### Programmatic Usage
You can also use Owl-Eye in your Python scripts:

```python
from owl_eye import display_banner, check_network, fetch_whois_data, extract_topics, extract_details

# Display banner
display_banner()

# Check network connectivity
if check_network():
    domain = "example.com"
    soup = fetch_whois_data(domain)

    # Extract and display WHOIS data
    extract_topics(soup, 0)  # Example topic
    extract_details(soup, 0)  # Example detail
```

---

## Requirements

The following Python packages are required:
- `colorama`
- `pyfiglet`
- `requests`
- `beautifulsoup4`

These will be installed automatically when you install Owl-Eye via pip.

---

## Project Structure
```plaintext
owl-eye/
├── owl_eye/
│   ├── __init__.py
│   ├── banner.py
│   ├── utils.py
│   ├── whois_lookup.py
│   ├── main.py
├── tests/
│   ├── test_banner.py
│   ├── test_utils.py
│   ├── test_whois_lookup.py
├── setup.py
├── README.md
├── LICENSE
├── requirements.txt
```

---

## Contribution

We welcome contributions to improve Owl-Eye! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Open a pull request describing your changes.

---

## Acknowledgments

This package is based on the original **Owl-Eye** tool developed by [LaviruD](https://github.com/LaviruD/Owl-Eye). Special thanks for their fantastic work on the original script.

---

## License

Owl-Eye is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute this software as per the license.

---

## Support

For issues or feature requests, please open an issue in the [GitHub repository](https://github.com/ishaoshada/Owl-Eye/issues).

