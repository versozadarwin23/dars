import requests
from bs4 import BeautifulSoup
import time
import random
import string
import os
from datetime import datetime
import re
import sys
import uuid
import hashlib
import subprocess
import re  # Added for regex support

IP = {"1-126, 128-191, 192, 99999"}
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"
LIGHT_PINK = "\033[95m"
PINK = "\033[91m"
MAGENTA = "\033[35m"
LIGHT_BLUE = "\033[94m"
PURPLE = "\033[35m"
WHITE = "\033[97m"
CYAN = "\033[96m"
RESET = "\033[0m"
# Constants
BASE_URL_KUKU = "https://m.kuku.lu"
LOGO = fr"""
{CYAN}
╔══════════════════════════════════════════════╗
║                                              ║
║     ██████╗  █████╗ ██████╗ ███████╗         ║
║    ██╔════╝ ██╔══██╗██╔══██╗██╔════╝         ║
║    ██║  ███╗███████║██████╔╝█████╗           ║
║    ██║   ██║██╔══██║██╔═══╝ ██╔══╝           ║
║    ╚██████╔╝██║  ██║██║     ███████╗         ║
║     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚══════╝         ║
║                                              ║
║       ⸻  Auto FB Creator by Darwin  ⸻        ║
╚══════════════════════════════════════════════╝
{RESET}
"""

MAX_RETRIES = 3
RETRY_DELAY = 2
# ANSI color codes

# Emojis and Symbols
SUCCESS = "✅"
FAILURE = "✅"
INFO = "✅"
WARNING = "⚠️"
LOADING = "⏳"

# Define the hashed password
HASHED_PASSWORD = hashlib.sha256("524932510194".encode()).hexdigest()

# Function to check the password

# Main function
if __name__ == "__main__":
    ua = [
        "Mozilla/5.0 (Linux; Android 11; SM-F926N Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-A217F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-A525M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-A705GM Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-A307FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-A127F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-A326B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; ONEPLUS A6013 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; POCO F2 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Infinix X697 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; moto g play (2021) Build/RZAS31.Q2-146-14-1-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.73 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-A307G Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 EdgW/1.0",
        "Mozilla/5.0 (Linux; Android 11; SM-A102N Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-A315G Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-J730G Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; OPPO CPH2025 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-M127F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-A302F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; OPPO CPH2027 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Xiaomi MI 10T Pro Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Galaxy A12 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Galaxy S20 FE Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-G980F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-A515F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; OnePlus 8T Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Motorola Edge Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Realme GT Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Vivo V21 5G Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Asus Zenfone 8 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; POCO M3 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Nokia 8.3 5G Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Sony Xperia 10 III Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Huawei P40 Pro Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Oppo Find X3 Pro Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36",
    ]

    user_agent = random.choice(ua)
    print(user_agent)

def get_cookies_kuku():
    """Fetch initial cookies from the email service."""
    url = f"{BASE_URL_KUKU}/en.php"
    headers = {
        "cache-control": "max-age=0",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "upgrade-insecure-requests": "1",
        "user-agent": user_agent,
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "referer": "https://www.google.com/",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9",
        "priority": "u=0, i"
    }

    while True:  # Start an infinite loop
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                cok = response.cookies.get_dict()
                if cok:  # If cookies are fetched
                    return cok
                else:
                    print(f"{RED}{FAILURE} No cookies received.{RESET}")
            else:
                print(f"{RED}{FAILURE} Failed to fetch cookies: {response.status_code}{RESET}")

            # If failed, wait for a while before trying again
            print("Retrying...")

        except Exception as e:
            print(f"{RED}{FAILURE} Error fetching cookies: {e}{RESET}")
            print("Retrying...")


def generate_email_kuku(cok):
    """Generate a random email using kuku.lu."""
    url = f"{BASE_URL_KUKU}/index.php"
    em = ''.join(random.choices(string.ascii_lowercase, k=18))
    sagmaw = 'boxfi.uk', 'haren.uk'
    wagas = random.choices(sagmaw)
    # addMailAddrByManual addMailAddrByAuto
    params = {
        "action": "addMailAddrByAuto",
        "nopost": "1",
        "by_system": "1",
        "t": str(int(time.time())),
        "csrf_token_check": cok.get("cookie_csrf_token", ""),
        "newdomain": wagas,
        "newuser": em,
        "recaptcha_token": "",
        "_": str(int(time.time() * 1000))
    }
    headers = {
        "sec-ch-ua-platform": '"Android 11"',
        "x-requested-with": "XMLHttpRequest",
        "user-agent": user_agent,
        "accept": "*/*",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "sec-ch-ua-mobile": "?1",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9",
        "priority": "u=1, i"
    }

    while True:
        try:
            response = requests.get(url, headers=headers, params=params, cookies=cok)
            if response.status_code == 200:
                if response.text.startswith("OK:"):
                    return response.text.split("OK:")[1].strip()
                else:
                    pass
            else:
                pass
        except requests.exceptions.ConnectionError:
            print(f"{RED}[{GREEN}•{RED}]{RESET} {RED}Connection error. Retrying in 15 seconds...{RESET}")
        except Exception as e:
            print(f"{RED}[{GREEN}•{RED}]{RESET} {RED}Error: {e}. Retrying in 15 seconds...{RESET}")


def check_otp_kuku(cok, max_attempts=5, delay=5):
    """Check for OTP in the email."""
    url = f"{BASE_URL_KUKU}/recv._ajax.php"
    params = {
        "nopost": "1",
        "csrf_token_check": cok.get("cookie_csrf_token", ""),
        "csrf_subtoken_check": cok.get("csrf_subtoken_check", ""),
        "_": str(int(time.time() * 1000))
    }
    headers = {
        "sec-ch-ua-platform": '"Android"',
        "x-requested-with": "XMLHttpRequest",
        "user-agent": user_agent,
        "accept": "*/*",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "sec-ch-ua-mobile": "?1",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "accept-encoding": "gzip, deflate,",
        "accept-language": "en-US,en;q=0.9",
        "priority": "u=1, i"
    }

    for attempt in range(max_attempts):
        try:
            while True:
                try:
                    response = requests.get(url, headers=headers, params=params, cookies=cok)
                    break
                except:
                    pass
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                subject_div = soup.find("div", id=lambda x: x and x.startswith("area_mail_title_"))
                if subject_div:
                    subject_text = subject_div.get_text(strip=True)
                    otp_match = re.search(r'FB-\s*(\d{4,6})|(\d{4,6})\s*is your confirmation code', subject_text)
                    if otp_match:
                        return otp_match.group(1) or otp_match.group(2)
                    else:
                        time.sleep(delay)
                else:
                    time.sleep(delay)
            else:
                time.sleep(delay)
        except requests.exceptions.ConnectionError:
            print(f"{RED}[{GREEN}•{RED}]{RESET} {RED}Connection error. Retrying in 15 seconds...{RESET}")
            time.sleep(15)
        except Exception as e:
            print(f"{RED}[{GREEN}•{RED}]{RESET} {RED}Error: {e}. Retrying in 15 seconds...{RESET}")
            time.sleep(15)

    return None


def load_names_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]


def get_names(account_type, gender):
    if account_type == 1:  # Philippines
        # Load male and last names from file (ensure correct file paths)
        male_first_names = load_names_from_file("/storage/emulated/0/Download/first_name.txt")
        last_names = load_names_from_file("/storage/emulated/0/Download/last_name.txt")
        female_first_names = []  # Female names not used for this account type
    else:  # Other account type
        male_first_names = []  # Not used
        female_first_names = load_names_from_file('path_to_female_first_names.txt')
        last_names = load_names_from_file('path_to_last_names.txt')

    # Select first name based on gender
    firstname = random.choice(male_first_names if gender == 1 else female_first_names)
    lastname = random.choice(last_names)

    return firstname, lastname


def generate_random_phone_number():
    """Generate a random phone number."""
    random_number = str(random.randint(1000000, 9999999))
    third = random.randint(0, 4)
    forth = random.randint(1, 7)
    phone_formats = [
        f"+639{third}{forth}{random_number}",
        f"+639{third}{forth}{random_number}",
    ]
    number = random.choice(phone_formats)

    return number


def generate_random_password():
    """Generate a random password with at least one letter, digit, and symbol."""
    letters = string.ascii_letters
    digits = string.digits

    # Ensure at least one character from each group
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(digits),
    ]

    # Fill the remaining characters randomly from all groups
    all_chars = letters + digits
    password += random.choices(all_chars, k=8)

    # Shuffle the result to avoid predictable positions
    random.shuffle(password)
    return ''.join(password)


def generate_user_details(account_type, gender):
    """Generate random user details."""
    firstname, lastname = get_names(account_type, gender)
    year = random.randint(1923, 2000)
    date = random.randint(1, 28)
    month = random.randint(1, 12)
    formatted_date = f"{date:02d}-{month:02d}-{year:04d}"
    password = generate_random_password()
    phone_number = generate_random_phone_number()
    return firstname, lastname, date, year, month, phone_number, password


def create_fbunconfirmed(account_type, usern, gender):
    """Create a Facebook account using kuku.lu for email and OTP."""

    asdf = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    ua = user_agent
    firstname, lastname, date, year, month, phone_number, password = generate_user_details(account_type, gender)
    username = firstname + lastname + asdf

    url = "https://limited.facebook.com/reg/?ref=dbl&soft=hjk"

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "dpr": "1",
        "priority": "u=0, i",
        "sec-ch-prefers-color-scheme": "dark",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "viewport-width": "720",
        "user-agent": ua
    }
    session = requests.Session()

    def retry_request(url, headers, method="get", data=None):
        global response
        while True:
            try:
                if method == "get":
                    response = session.get(url, headers=headers)
                elif method == "post":
                    response = session.post(url, headers=headers, data=data)
                return response
            except requests.exceptions.ConnectionError:
                time.sleep(3)
                print(f"{RED}{FAILURE} Connection error, retrying in 15 seconds...{RESET}")

    # Step 1: Initialize session and get the registration form
    while True:
        try:
            response = retry_request(url, headers)
            soup = BeautifulSoup(response.text, "html.parser")
            form = soup.find("form")
            break
        except:
            pass

    # Assume 'form' is a BeautifulSoup object of the form
    # Get kuku.lu email
    cok = get_cookies_kuku()
    email = generate_email_kuku(cok)

    lastnamess = load_names_from_file("/storage/emulated/0/Download/last_name.txt")
    ncs = random.choice(lastnamess)
    dawdaw = ncs + password
    data = {
        "firstname": firstname,
        "lastname": lastname,
        "birthday_day": date,
        "birthday_month": month,
        "birthday_year": year,
        "reg_email__": email,
        "sex": gender,
        "reg_passwd__": dawdaw,
        "submit": "Sign Up"
    }
    # Add hidden inputs to the data dictionary
    hidden_inputs = form.find_all("input")
    for inp in hidden_inputs:

        if inp.has_attr("name"):
            time.sleep(5)
            data[inp["name"]] = inp.get("value", "")
    response = session.post(url, data=data, headers=headers, cookies=cok, allow_redirects=True)
    time.sleep(10)
    if "c_user" in session.cookies:
        uid = session.cookies.get("c_user")
        profile_id = 'https://www.facebook.com/profile.php?id=' + uid
        cook = ";".join([f"{key}={value}" for key, value in session.cookies.items()])
        confirmation_code = check_otp_kuku(cok)
        if confirmation_code:
            sys.stdout.write(
                f'\r\033[K{RESET}: {CYAN}|{firstname} {lastname}|{GREEN}{uid}|{dawdaw}|{confirmation_code}|{RESET}\n')
            sys.stdout.flush()
            open("/storage/emulated/0/Download/acc.txt", "a").write(f"{phone_number}|{dawdaw}|{confirmation_code}|{profile_id}|\n")
            return uid, password, confirmation_code, cook, email
        else:
            print(f"{RED}No confirmation code found.{RESET}")
            return None

    else:
        print(f"{RED}Account creation failed.{RESET}")
        return None



def NEMAIN():
    """Handles new registration method automatically."""

    max_create = 1  # Set how many accounts to generate
    account_type = 1  # 1 = Philippines
    gender = 1  # 1 = Male, 2 = Female
    # --------------------------------------
    oks = []
    cps = []

    for i in range(max_create):
        # Show progress
        sys.stdout.write(f'\r\33[38;5;82m  [\x1b[38;5;82m{CYAN}Creating Acc Please Wait.\33[38;5;82m]\033[1;97m - \33[38;5;82m[\033[1;97m{i + 1}/{max_create}\33[38;5;82m]')
        sys.stdout.flush()
        usern = "auto_user"  # Can be customized if needed
        result = create_fbunconfirmed(account_type, usern, gender)

        if result:
            oks.append(result)
        else:
            cps.append(result)

    print(f"{BLUE}{INFO}   Batch creation completed{RESET}")


# Run the main function
if __name__ == "__main__":
    print(LOGO)
    NEMAIN()
