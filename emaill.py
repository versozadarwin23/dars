import os

import requests
from bs4 import BeautifulSoup
import time
import random
import string
from datetime import datetime
import sys
import re

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
 _____ ___ ____  _   _ ____   ___   ___  _  __  ____ ___  __  __ 
|  ___|_ _/ ___|| | | | __ ) / _ \ / _ \| |/ / / ___/ _ \|  \/  |
| |_   | |\___ \| |_| |  _ \| | | | | | | ' / | |  | | | | |\/| |
|  _|  | | ___) |  _  | |_) | |_| | |_| | . \ | |__| |_| | |  | |
|_|   |___|____/|_| |_|____/ \___/ \___/|_|\_(_)____\___/|_|  |_|
                                                        KUPAL.COM{YELLOW}
═════════════════════════════════════════════════════════════════
   {RED}[{GREEN}•{RED}]{RESET}   Owner   : {CYAN}Call me Mark
   {RED}[{GREEN}•{RED}]{RESET}   Tool    : FISHBOOK.COM                                    
   {RED}[{GREEN}•{RED}]{RESET}   Contact : {CYAN}t.me/Lumagdazz
   {RED}[{GREEN}•{RED}]{RESET}   Version : {GREEN}1.5 {YELLOW} {RESET}
   {RED}[{GREEN}•{RED}]{RESET}   Network : 4G/WIFI DYNAMIC ONLY
   {RED}[{GREEN}•{RED}]{RESET}   Note    : Do at your own RISK!
   {RED}[{GREEN}•{RED}]{RESET}   IP Address  :{GREEN}"Class A, B, C" {RESET}
    Use Facebook lite only! if suspended uninstall and install
    Airplane mode 10 seconds 

{YELLOW}   
═════════════════════════════════════════════════════════════════
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


def generate_old_android_ua():
    """Generate an old Android user agent."""
    random.seed(datetime.now().timestamp())
    android_versions = [
        ("11", "RQ1A.210205.003"),
        ("11", "RP1A.200720.012"),
        ("11", "RQP1.210122.002"),
        ("11", "RP1A.200720.009"),
        ("11", "RPE1.200720.011")
    ]

    # List of Android 11 devices
    devices = [
        ("Pixel 5", "Google"),
        ("Pixel 4a", "Google"),
        ("Pixel 4", "Google"),
        ("Galaxy S20", "Samsung"),
        ("Galaxy Note 20", "Samsung"),
        ("OnePlus 8", "OnePlus"),
        ("OnePlus 8T", "OnePlus"),
        ("Xperia 1 II", "Sony"),
        ("Xiaomi Mi 10", "Xiaomi"),
        ("Oppo Reno4", "Oppo")
    ]

    android_ver, android_code = random.choice(android_versions)
    device, manufacturer = random.choice(devices)

    build_number = f"{android_code}"
    if android_ver.startswith("4.0"):
        build_number += f".{random.choice(['IMM76', 'GRK39', 'IMM76D'])}"
    else:
        build_number += random.choice(["D", "E", "F"]) + str(random.randint(10, 99))

    chrome_major = random.randint(
        18 if android_ver.startswith("4.0") else 25,
        35 if android_ver.startswith("4.4") else 32
    )
    chrome_build = random.randint(1000, 1999)
    chrome_patch = random.randint(50, 199)

    webkit_base = "534.30" if chrome_major < 25 else "537.36"
    webkit_ver = f"{webkit_base}.{random.randint(1, 99)}" if random.random() > 0.7 else webkit_base

    ua = (
        f"Mozilla/5.0 (Linux; Vivo Y11 {android_ver}; {device} Build/{build_number}) "
        f"AppleWebKit/{webkit_ver} (KHTML, like Gecko) "
        f"Chrome/{chrome_major}.0.{chrome_build}.{chrome_patch} Mobile Safari/{webkit_ver.split('.')[0]}.0"
    )

    return ua


def get_cookies_kuku():
    url = f"{BASE_URL_KUKU}/en.php"
    headers = {
        "cache-control": "max-age=0",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "upgrade-insecure-requests": "1",
        "user-agent": generate_old_android_ua(),
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

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            cok = response.cookies.get_dict()
            return cok
        else:
            print(f"{RED}{FAILURE} Failed to fetch cookies: {response.status_code}{RESET}")
            return None
    except Exception as e:
        print(f"{RED}{FAILURE} Error fetching cookies: {e}{RESET}")
        return None


def generate_email_kuku(cok):
    """Generate a random email using kuku.lu."""
    url = f"{BASE_URL_KUKU}/index.php"
    em = ''.join(random.choices(string.ascii_lowercase, k=18))
    #addMailAddrByManual
    #addMailAddrByAuto
    sagma = 'boxfi.uk', 'haren.uk'
    hahi = random.choice(sagma)
    params = {
        "action": "addMailAddrByAuto",
        "nopost": "1",
        "by_system": "1",
        "t": str(int(time.time())),
        "csrf_token_check": cok.get("cookie_csrf_token", ""),
        # "newdomain": hahi,
        "newuser": em,
        "recaptcha_token": "",
        "_": str(int(time.time() * 1000))
    }
    headers = {
        "sec-ch-ua-platform": '"Android"',
        "x-requested-with": "XMLHttpRequest",
        "user-agent": generate_old_android_ua(),
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
        except requests.exceptions.ConnectionError:
            print(f"{RED}[{GREEN}•{RED}]{RESET} {RED}Connection error. Retrying in 3 seconds...{RESET}")
            time.sleep(3)
        except Exception as e:
            print(f"{RED}[{GREEN}•{RED}]{RESET} {RED}Error: {e}. Retrying in 3 seconds...{RESET}")
            time.sleep(3)


def check_otp_kuku(email, cok, max_attempts=10, delay=3):
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
        "user-agent": generate_old_android_ua(),
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
            response = requests.get(url, headers=headers, params=params, cookies=cok)
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
            print(f"{RED}[{GREEN}•{RED}]{RESET} {RED}Connection error. Retrying in 3 seconds...{RESET}")
            time.sleep(3)
        except Exception as e:
            print(f"{RED}[{GREEN}•{RED}]{RESET} {RED}Error: {e}. Retrying in 3 seconds...{RESET}")
            time.sleep(3)

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
        f"09{third}{forth}{random_number}",
        f"09{third}{forth}{random_number}",
    ]
    number = random.choice(phone_formats)

    return number


def generate_random_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    return password


def generate_user_details(account_type, gender):
    """Generate random user details."""
    firstname, lastname = get_names(account_type, gender)
    year = random.randint(1978, 2001)
    date = random.randint(1, 28)
    month = random.randint(1, 12)
    password = generate_random_password()
    phone_number = generate_random_phone_number()
    return firstname, lastname, date, year, month, phone_number, password


def create_fbunconfirmed(account_type, usern, gender):
    """Create a Facebook account using kuku.lu for email and OTP."""

    global uid, profie_link
    asdf = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    ua = generate_old_android_ua()
    firstname, lastname, date, year, month, phone_number, password = generate_user_details(account_type, gender)

    def check_page_loaded(url, headers):
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        form = soup.find("form")
        return form

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:84.0) Gecko/20100101 Firefox/84.0",
        "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; AS; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/92.0.902.67 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/88.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.67 Safari/537.36",
        # ... Add all other User-Agents here in the same way
    ]

    # Randomly choose a User-Agent
    random_user_agent = random.choice(user_agents)

    url = "https://m.facebook.com/reg/?is_two_steps_login=0&cid=103&refsrc=deprecated&soft=hjk"
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
        "user-agent": random_user_agent,
        # "viewport-width": "720"
    }

    session = requests.Session()

    # Polling loop
    while True:
        form = check_page_loaded(url, headers)
        if form:
            break  # Exit loop if form is found
        else:
            print("Waiting for form to load...")
            time.sleep(3)  # Wait for 3 seconds before checking again

    # Retry request function
    def retry_request(url, headers, method="get", data=None):
        while True:
            try:
                if method == "get":
                    response = session.get(url, headers=headers)
                elif method == "post":
                    response = session.post(url, headers=headers, data=data)
                # Check for successful response
                if response.status_code == 200:
                    return response
                else:
                    print(f"Unexpected status code: {response.status_code}, retrying in 3 seconds...")
            except requests.exceptions.ConnectionError:
                print("Connection error, retrying in 3 seconds...")
            time.sleep(3)

    response = retry_request(url, headers)
    soup = BeautifulSoup(response.text, "html.parser")
    form = soup.find("form")

    if form:
        action_url = requests.compat.urljoin(url, form["action"]) if form.has_attr("action") else url
        inputs = form.find_all("input")
        data = {
            "firstname": f"{firstname}",
            "lastname": f"{lastname}",
            "birthday_day": f"{date}",
            "birthday_month": f"{month}",
            "birthday_year": f"{year}",
            "reg_email__": f"{phone_number}",
            "sex": f"{gender}",
            "encpass": f"{password}",
            "submit": "Sign Up"
        }

        for inp in inputs:
            if inp.has_attr("name") and inp["name"] not in data:
                data[inp["name"]] = inp["value"] if inp.has_attr("value") else ""

        # Step 2: Submit the registration form
        submit_response = retry_request(action_url, headers, method="post", data=data)

        if "c_user" in session.cookies:
            uid = session.cookies.get("c_user")
            profie_link = 'https://m.facebook.com/' + uid

    # Step 3: Change email
    change_email_url = "https://m.facebook.com/changeemail/"
    email_response = retry_request(change_email_url, headers)
    soup = BeautifulSoup(email_response.text, "html.parser")
    form = soup.find("form")

    if form:
        action_url = requests.compat.urljoin(change_email_url, form["action"]) if form.has_attr(
            "action") else change_email_url
        inputs = form.find_all("input")
        data = {}
        for inp in inputs:
            if inp.has_attr("name") and inp["name"] not in data:
                data[inp["name"]] = inp["value"] if inp.has_attr("value") else ""

        # Generate email using kuku.lu
        cok = get_cookies_kuku()
        email = generate_email_kuku(cok)
        data["new"] = email
        data["submit"] = "Add"

        # Step 4: Submit email change form
        submit_response = retry_request(action_url, headers, method="post", data=data)
        confirmation_code = check_otp_kuku(email, cok)
        cook = ";".join([f"{key}={value}" for key, value in session.cookies.items()])
        if confirmation_code:
            sys.stdout.write(f'\r\033[K{RESET}{CYAN}{firstname} {lastname}|{GREEN}{phone_number}|{password}|{confirmation_code}{RESET}\n')
            sys.stdout.flush()
            folder_path = "/storage/emulated/0/Download/"
            file_path = os.path.join(folder_path, "created_acc.txt")

            # Create folder if it doesn't exist
            os.makedirs(folder_path, exist_ok=True)

            # Write to the file
            with open(file_path, "a") as f:
                

            
            response = requests.get(confirmation_codesss, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            

            return uid, firstname, confirmation_code, cook, email

def NEMAIN():
    os.system("clear")
    max_create = 5
    account_type = 1
    gender = 1
    oks = []
    cps = []
    for i in range(max_create):
        usern = "ali"  # Replace with actual username logic
        result = create_fbunconfirmed(account_type, usern, gender)

        if result:
            oks.append(result)
        else:
            cps.append(result)

    print(f"{BLUE}{INFO}   Batch creation completed{RESET}")

# Run the main function
if __name__ == "__main__":
    NEMAIN()
