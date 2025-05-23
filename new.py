import os
import uuid
import requests
from bs4 import BeautifulSoup
import time
import sys
import random
from fake_useragent import UserAgent
ua = UserAgent()

def load_user_agents(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        user_agents = [line.strip() for line in file if line.strip()]
    return user_agents

def get_random_user_agent(file_path):
    user_agents = load_user_agents(file_path)
    return random.choice(user_agents)

# Example usage:

MAX_RETRIES = 3
RETRY_DELAY = 2
# ANSI color codes

# Emojis and Symbols
SUCCESS = "✅"
FAILURE = "✅"
INFO = "✅"
WARNING = "⚠️"
LOADING = "⏳"

def load_names_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]


def get_names(account_type, gender):
    if account_type == 1:  # Philippines
        # Load male and last names from file (ensure correct file paths)
        male_first_names = load_names_from_file("first_name.txt")
        last_names = load_names_from_file("last_name.txt")
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

    # Ensure at least one symbol is included (only if base is short enough, which it's not)
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

    global uid, profie_link, profile_link
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

    url = "https://m.facebook.com/reg?soft=hjk&_rdr"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        # "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://m.facebook.com/",
        "Connection": "keep-alive",
        "X-FB-Connection-Type": "MOBILE.LTE",
        "X-FB-Connection-Quality": "EXCELLENT",
        "X-FB-Net-HNI": "51502",  # Smart PH
        "X-FB-SIM-HNI": "51502",
        "X-FB-HTTP-Engine": "Liger",
        'x-fb-connection-type': 'Unknown',
        'accept-encoding': 'gzip, deflate',
        'content-type': 'application/x-www-form-urlencoded',
        'x-fb-http-engine': 'Liger',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1903 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/444.0.0.0.110;]',
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
    # # Save entire page as HTML
    # with open('confirmation_page.html', 'w', encoding='utf-8') as f:
    #     f.write(soup.prettify())
    # print("Saved HTML successfully.")

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
                # time.sleep(random.uniform(3, 5))
                data[inp["name"]] = inp["value"] if inp.has_attr("value") else ""

        # Step 2: Submit the registration form
        submit_response = retry_request(action_url, headers, method="post", data=data)
        try:
            if "c_user" in session.cookies:
                uid = session.cookies.get("c_user")
                profile_link = 'https://www.facebook.com/profile.php?id=' + uid
            else:
                print("Login failed.")
                sys.exit()  # exit if not logged in
        except Exception as e:
            print("An error occurred:", str(e))
            sys.exit()


    while True:
        try:
            # Step 3: Change email
            change_email_url = "https://m.facebook.com/changeemail/"
            headerssss = {
                "sec-ch-ua-platform": '"Android"',
                "x-requested-with": "XMLHttpRequest",
                "accept": "*/*",
                'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1903 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/444.0.0.0.110;]',
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
                emailsss = input("Please enter your email: ")
                data["new"] = emailsss
                data["submit"] = "Add"
                break
            except:
                pass

        # Step 4: Submit email change form
        retry_request(action_url, headers, method="post", data=data)
        if "c_user" in session.cookies:
            sys.stdout.write(f'\r\033[K{firstname} {lastname}|{phone_number}|{password}|\n')
            sys.stdout.flush()
            headerssss = {
                "sec-ch-ua-platform": '"Android"',
                "x-requested-with": "XMLHttpRequest",
                "accept": "*/*",
                "user-agent": ua['Chrome'],
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?1",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "accept-encoding": "gzip, deflate,",
                "accept-language": "en-US,en;q=0.9",
                "priority": "u=1, i"
            }
            url = "https://www.facebook.com"
            fewsa = session.get(url, headers=headerssss)
            soup = BeautifulSoup(fewsa.text, "html.parser")
            form = soup.find("form")
            # with open('confirmation_page.html', 'w', encoding='utf-8') as f:
            #     f.write(soup.prettify())
            # print("Saved HTML successfully.")
            action_url = form.get("action")
            csrf_token = form.find("input", {"name": "fb_dtsg"})["value"]
            codesss = input("Please enter your code: ")
            form_data = {
                "code": codesss,
                "fb_dtsg": csrf_token,
            }

            delay_seconds = random.uniform(3, 5)
            time.sleep(delay_seconds)
            submit_url = f"https://www.facebook.com{action_url}" if action_url.startswith("/") else action_url
            session.post(submit_url, data=form_data)

            now = int(time.time())
            random_offset = random.randint(-86400 * 1, 0)  # Up to 1 day ago
            fake_timestamp = str(now + random_offset)

            # Generate a random fake IPv4 address
            fake_ip = "{}.{}.{}.{}".format(
                random.randint(1, 254),
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(1, 254)
            )

            # Base headers (without IP and timestamp)
            base_headers = {
                'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'User-Agent': '[FBAN/FB4A;FBAV/388.0.0.21.107;FBBV/469533592;FBDM/{density=2.0,width=720,height=1520};FBLC/en_US;FBRV/0;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.lite;FBDV/SM-A107F;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi]',
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "X-FB-Net-HNI": "51502",
                "X-FB-SIM-HNI": "51502",
                "X-FB-HTTP-Engine": "Liger",
                "Accept-Language": "en-US,en;q=0.5",
                'x-fb-friendly-name': 'Authenticate',
                'x-fb-connection-type': 'Unknown',
                'accept-encoding': 'gzip, deflate',
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger',
            }

            # Prepare headers
            headers = base_headers.copy()
            headers['X-Forwarded-For'] = fake_ip
            headers['Client-IP'] = fake_ip
            headers['x-fb-request-time'] = fake_timestamp

            # Prepare form data
            data = {
                'email': uid,
                'password': password,
                'credentials_type': 'password',
                'adid': ''.join(random.choices(string.hexdigits, k=16)),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'generate_analytics_claims': '0',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '0',
                'generate_machine_id': '0',
                'fb_api_req_friendly_name': 'authenticate',
            }

            # Send request
            try:
                response = requests.post('https://b-graph.facebook.com/auth/login', headers=headers, data=data)
                try:
                    result = response.json()
                except Exception:
                    print(f"\033[91m[!] Failed to parse JSON. Raw response:\033[0m\n{response.text}")
                    result = None

                if result:
                    if 'access_token' in result:
                        token = result['access_token']
                        print(f"\033[92mtoken: {token}\033[0m")
                        with open("tokens.txt", "w", encoding="utf-8") as token_file:
                            token_file.write(f"{emailsss} {password} | {token}\n")
                    elif 'error' in result:
                        error = result['error']
                        user_msg = error.get('error_user_msg', error.get('message', str(error)))
                        print(f"\033[91m[-] {emailsss} {password} | {user_msg}\033[0m")
                    else:
                        print(f"\033[93m[?] {emailsss} {password} | Unexpected response: {result}\033[0m")

            except Exception as e:
                print(f"\033[91m[!] {emailsss} {password} | Exception: {e}\033[0m")
                if 'response' in locals():
                    print(f"Response text: {response.text}")
                else:
                    print("No response")

            sys.stdout.write(f'\r\033[K{firstname} {lastname}|{phone_number}|{password}|\n')

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

    print(f"{INFO}   Batch creation completed")

# Run the main function
if __name__ == "__main__":
    NEMAIN()
