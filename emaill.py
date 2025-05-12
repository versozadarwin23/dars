import os

import requests
from bs4 import BeautifulSoup
import time
import random
import string
from datetime import datetime
import sys
import re

android_11_user_agents = [
    "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.0 Chrome/92.0.4515.131 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 3a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4147.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A025G) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
    "Mozilla/5.0 (Linux; Android 11; SM-A426U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-M127N) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G9910) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G998W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; moto g(10) power Build/RRBS31.Q1-3-34-1-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; moto g(50) Build/RRFS31.Q1-59-76-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36 EdgW/1.0",
    "Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Nokia G20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2108) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2045) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; M2102J20SG Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; M2103K19PG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.3",
    "Mozilla/5.0 (Linux; Android 11; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2001 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A525M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/349.0.0.7.108;]",
    "Mozilla/5.0 (Linux; Android 11; Infinix X697 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Infinix X658E Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; ONEPLUS A6013 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G998W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G9910) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2108) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2045) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Nokia G20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36",
    # Add more entries here for 100+ user agents...
    ]

# Pick a random User-Agent
random_user_agentsss = random.choice(android_11_user_agents)


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

def get_cookies_kuku():
    url = f"{BASE_URL_KUKU}/en.php"
    headers = {
        "cache-control": "max-age=0",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "upgrade-insecure-requests": "1",
        "user-agent": random_user_agentsss,
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
    while True:
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                cok = response.cookies.get_dict()
                return cok
            else:
                print(f"{RED}{FAILURE} Failed to fetch cookies: {response.status_code}{RESET}")
                break
        except Exception as e:
            print(f"{RED}{FAILURE} Error fetching cookies: {e}{RESET}")

def generate_email_kuku(cok):
    """Keep generating a kuku.lu email until success."""
    sagma = ['boxfi.uk', 'haren.uk']

    while True:
        try:
            url = "https://m.kuku.lu/index.php"
            em = ''.join(random.choices(string.ascii_lowercase, k=18))
            hahi = random.choice(sagma)
            timestamp = str(int(time.time()))
            params = {
                "action": "addMailAddrByAuto",
                "user-agent": "Mozilla/5.0 (Linux; Android 11; Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5124.165 Mobile Safari/537.36",
                "nopost": "1",
                "by_system": "1",
                "t": timestamp,
                "csrf_token_check": cok.get("cookie_csrf_token", ""),
                "newuser": em,
                "recaptcha_token": "",
                "_": str(int(time.time() * 1000))
            }

            headers = {
                "sec-ch-ua-platform": '"Android"',
                "x-requested-with": "XMLHttpRequest",
                "user-agent": random_user_agentsss,
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

            response = requests.get(url, headers=headers, params=params, cookies=cok)

            if response.status_code == 200 and response.text.startswith("OK:"):
                return response.text.split("OK:")[1].strip()
            else:
                print("⏳ Retry: Did not receive OK response. Retrying in 3 seconds...")
                time.sleep(3)

        except requests.exceptions.ConnectionError:
            print("❌ Connection error. Retrying in 3 seconds...")
            time.sleep(3)
        except Exception as e:
            print(f"⚠️ Error: {e}. Retrying in 3 seconds...")
            time.sleep(3)


def check_otp_kuku(email, cok, max_attempts=10, delay=10):
    """Check for OTP in the email."""
    url = f"{BASE_URL_KUKU}/recv._ajax.php"
    params = {
        "nopost": "1",
        "csrf_token_check": cok.get("cookie_csrf_token", ""),
        "csrf_subtoken_check": cok.get("csrf_subtoken_check", ""),
        "_": str(int(time.time() * 1000))
    }
    headers = {
        "sec-ch-ua-platform": "Android",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": random_user_agentsss,
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
            response = requests.get(url, params=params, cookies=cok)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                subject_div = soup.find("div", id=lambda x: x and x.startswith("area_mail_title_"))
                print('otp waiting')
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


def load_names_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]


def get_names(account_type, gender):
    if account_type == 1:  # Philippines
        # Load male and last names from file (ensure correct file paths)
        male_first_names = load_names_from_file("/storage/emulated/0/Download/first_name.txtfirst_name.txt")
        last_names = load_names_from_file("/storage/emulated/0/Download/first_name.txtlast_name.txt")
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
        f"9{third}{forth}{random_number}",
        f"9{third}{forth}{random_number}",
    ]
    number = random.choice(phone_formats)

    return number


import random
import string

def generate_random_password():
    base = 'Promises'  # fixed part
    symbols = '!@#$%^&*()_+-='
    remaining_length = 3 - len(base)

    # Make sure at least one symbol is included
    if remaining_length > 0:
        mixed_chars = string.digits + symbols
        extra = ''.join(random.choices(mixed_chars, k=remaining_length - 1))
        extra += random.choice(symbols)  # ensure at least one symbol
        extra = ''.join(random.sample(extra, len(extra)))  # shuffle extra chars
    else:
        extra = ''

    six_digit = str(random.randint(100000, 999999))  # random 6-digit number
    password = base + extra + six_digit
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
    firstname, lastname, date, year, month, phone_number, password = generate_user_details(account_type, gender)

    def check_page_loaded(url, headers):
        while True:
            try:
                response = requests.get(url, headers=headers)
                soup = BeautifulSoup(response.text, 'html.parser')
                form = soup.find("form")
                return form
            except:
                print('error')
                pass

    url = "https://m.facebook.com/reg"
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
        "user-agent": random_user_agentsss,
        "viewport-width": "720"
    }

    while True:
        try:
            session = requests.Session()
            break
        except:
            print('seasion error')
            pass

    # # Save entire page as HTML
    # with open('confirmation_page.html', 'w', encoding='utf-8') as f:
    #     f.write(soup.prettify())
    # print("Saved HTML successfully.")
    # Polling loop
    while True:
        form = check_page_loaded(url, headers)
        if form:
            break  # Exit loop if form is found
        else:
            print("Waiting for form to load...")
            time.sleep(3)  # Wait for 3 seconds before checking again

    # # Save entire page as HTML
    # with open('confirmation_page.html', 'w', encoding='utf-8') as f:
    #     f.write(soup.prettify())
    # print("Saved HTML successfully.")


    # Retry request function
    def retry_request(url, headers, method="get", data=None):
        global response
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
            time.sleep(15)

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
            profie_link = 'https://www.facebook.com/profile.php?id=' + uid
            print(phone_number + " " + password + " " + profie_link)



    while True:
        try:
            # Step 3: Change email
            change_email_url = "https://m.facebook.com/changeemail/"

            headerssss = {
                "sec-ch-ua-platform": '"Android"',
                "x-requested-with": "XMLHttpRequest",
                "user-agent": random_user_agentsss,
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

            email_response = retry_request(change_email_url, headerssss)
            soup = BeautifulSoup(email_response.text, "html.parser")
            form = soup.find("form")
            break
        except:
            pass

    if form:
        action_url = requests.compat.urljoin(change_email_url, form["action"]) if form.has_attr(
            "action") else change_email_url
        inputs = form.find_all("input")
        data = {}
        for inp in inputs:
            if inp.has_attr("name") and inp["name"] not in data:
                time.sleep(random.uniform(3, 5))
                data[inp["name"]] = inp["value"] if inp.has_attr("value") else ""
        while True:
            try:
                # Generate email using kuku.lu
                cok = get_cookies_kuku()
                email = generate_email_kuku(cok)
                data["new"] = email
                data["submit"] = "Add"
                break
            except:
                pass

        # Step 4: Submit email change form
        retry_request(action_url, headers, method="post", data=data)
        confirmation_code = check_otp_kuku(email, cok)
        cook = ";".join([f"{key}={value}" for key, value in session.cookies.items()])
        if confirmation_code:
            sys.stdout.write(f'\r\033[K{RESET}{CYAN}{firstname} {lastname}|{GREEN}{phone_number}|{password}|{confirmation_code}{RESET}\n')
            sys.stdout.flush()
            # Step 1: GET the page
            url = "https://www.facebook.com"  # Or the exact page with the form
            response = session.get(url)
            # # Save entire page as HTML
            # with open('confirmation_page.html', 'w', encoding='utf-8') as f:
            #     f.write(soup.prettify())
            # print("Saved HTML successfully.")
            soup = BeautifulSoup(response.text, "html.parser")

            # Step 3: Extract any necessary form fields (e.g., CSRF tokens)
            form = soup.find("form")  # You may need to refine this selector
            action_url = form.get("action")

            # CSRF token example (not guaranteed; inspect your form)
            csrf_token = form.find("input", {"name": "fb_dtsg"})["value"]

            # Step 4: Prepare form data
            form_data = {
                "code": confirmation_code,  # <-- The code you want to submit
                "fb_dtsg": csrf_token,  # <-- If required
                # Add other hidden fields if necessary
            }

            # Step 5: POST the data
            delay_seconds = random.uniform(10, 20)  # random delay between 2 to 5 seconds
            time.sleep(delay_seconds)
            submit_url = f"https://www.facebook.com{action_url}" if action_url.startswith("/") else action_url
            session.post(submit_url, data=form_data)

            folder_path = "/storage/emulated/0/Download/first_name.txt"
            file_path = os.path.join(folder_path, "created_acc.txt")

            # Create folder if it doesn't exist
            os.makedirs(folder_path, exist_ok=True)

            # Write to the file
            with open(file_path, "a") as f:
                f.write(f"{firstname} {lastname}\t{phone_number}\t{password}\t{profie_link}\n")
            return uid, firstname, confirmation_code, cook, email

def NEMAIN():
    os.system("clear")
    max_create = 1
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
