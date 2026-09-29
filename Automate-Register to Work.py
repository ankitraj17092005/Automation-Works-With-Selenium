from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import random

indian_male_names = [
    "Aarav Sharma",
    "Aditya Kumar",
    "Arjun Singh",
    "Rahul Verma",
    "Rohit Gupta",
    "Ankit Raj",
    "Aman Mishra",
    "Vivek Yadav",
    "Karan Mehta",
    "Ravi Kumar",
    "Sahil Kapoor",
    "Abhishek Tiwari",
    "Akash Patel",
    "Nikhil Jain",
    "Saurabh Singh",
    "Manish Kumar",
    "Varun Sharma",
    "Rajat Verma",
    "Mohit Agarwal",
    "Deepak Yadav",
    "Pranav Joshi",
    "Rishabh Gupta",
    "Vikas Singh",
    "Harsh Vardhan",
    "Ayush Pandey",
    "Shubham Kumar",
    "Gaurav Mishra",
    "Yash Malhotra",
    "Piyush Sinha",
    "Devendra Singh"
]

indian_female_names = [
    "Aanya Sharma",
    "Ananya Singh",
    "Priya Kumar",
    "Neha Verma",
    "Pooja Gupta",
    "Riya Sharma",
    "Sneha Mishra",
    "Kavya Singh",
    "Simran Kaur",
    "Shreya Mehta",
    "Anjali Yadav",
    "Nisha Patel",
    "Swati Jain",
    "Isha Kapoor",
    "Divya Tiwari",
    "Aditi Joshi",
    "Megha Agarwal",
    "Ritika Singh",
    "Pallavi Kumar",
    "Sakshi Verma",
    "Muskan Gupta",
    "Komal Sharma",
    "Tanvi Mishra",
    "Priyanka Yadav",
    "Nandini Singh",
    "Payal Sinha",
    "Rashmi Kumari",
    "Kriti Pandey",
    "Mansi Mehta",
    "Shalini Sharma"
]
bihar_addresses = [
    "12 Ashok Nagar Road, Patna, Bihar",
    "45 Rajendra Nagar Road, Patna, Bihar",
    "78 Kankarbagh Main Road, Patna, Bihar",
    "23 Boring Road, Patna, Bihar",
    "91 Bailey Road, Patna, Bihar",
    "34 Exhibition Road, Patna, Bihar",
    "56 Fraser Road, Patna, Bihar",
    "17 Patliputra Colony Road, Patna, Bihar",
    "82 Danapur Road, Patna, Bihar",
    "29 Gandhi Maidan Road, Patna, Bihar",
    "63 Station Road, Gaya, Bihar",
    "41 Swarajpuri Road, Gaya, Bihar",
    "76 Main Road, Muzaffarpur, Bihar",
    "18 Club Road, Muzaffarpur, Bihar",
    "52 Circular Road, Bhagalpur, Bihar",
    "37 Tilkamanjhi Road, Bhagalpur, Bihar",
    "84 Hospital Road, Darbhanga, Bihar",
    "25 Laheriasarai Road, Darbhanga, Bihar",
    "69 Station Road, Bihar Sharif, Bihar",
    "31 Ramchandrapur Road, Bihar Sharif, Bihar"
]

jharkhand_addresses = [
    "14 Harmu Road, Ranchi, Jharkhand",
    "38 Main Road, Ranchi, Jharkhand",
    "72 Doranda Road, Ranchi, Jharkhand",
    "25 Kanke Road, Ranchi, Jharkhand",
    "61 Lalpur Road, Ranchi, Jharkhand",
    "47 Bariatu Road, Ranchi, Jharkhand",
    "83 Circular Road, Ranchi, Jharkhand",
    "19 Ashok Nagar Road, Ranchi, Jharkhand",
    "54 Sakchi Main Road, Jamshedpur, Jharkhand",
    "36 Bistupur Road, Jamshedpur, Jharkhand",
    "91 Mango Road, Jamshedpur, Jharkhand",
    "27 Sonari Road, Jamshedpur, Jharkhand",
    "65 Bank More Road, Dhanbad, Jharkhand",
    "42 Saraidhela Road, Dhanbad, Jharkhand",
    "78 Hirapur Road, Dhanbad, Jharkhand",
    "16 Court Road, Hazaribagh, Jharkhand",
    "53 Main Road, Hazaribagh, Jharkhand",
    "29 Station Road, Bokaro, Jharkhand",
    "81 City Centre Road, Bokaro, Jharkhand",
    "46 Main Road, Deoghar, Jharkhand"
]

uttar_pradesh_addresses = [
    "21 Gomti Nagar Road, Lucknow, Uttar Pradesh",
    "56 Hazratganj Road, Lucknow, Uttar Pradesh",
    "73 Aliganj Main Road, Lucknow, Uttar Pradesh",
    "18 Indira Nagar Road, Lucknow, Uttar Pradesh",
    "92 Mahanagar Road, Lucknow, Uttar Pradesh",
    "35 Vikas Nagar Road, Lucknow, Uttar Pradesh",
    "64 Civil Lines Road, Prayagraj, Uttar Pradesh",
    "27 George Town Road, Prayagraj, Uttar Pradesh",
    "81 MG Road, Agra, Uttar Pradesh",
    "43 Kamla Nagar Road, Agra, Uttar Pradesh",
    "69 Taj Nagari Road, Agra, Uttar Pradesh",
    "15 Swaroop Nagar Road, Kanpur, Uttar Pradesh",
    "58 Mall Road, Kanpur, Uttar Pradesh",
    "32 Kakadeo Road, Kanpur, Uttar Pradesh",
    "76 Gomti Nagar Extension, Lucknow, Uttar Pradesh",
    "24 Sigra Road, Varanasi, Uttar Pradesh",
    "87 Lanka Road, Varanasi, Uttar Pradesh",
    "49 Indira Nagar Road, Ghaziabad, Uttar Pradesh",
    "62 Sector 18 Road, Noida, Uttar Pradesh",
    "39 Sector 62 Road, Noida, Uttar Pradesh"
]


delhi_addresses = [
    "12 Model Town Road, Delhi",
    "45 Rohini Sector 7 Road, Delhi",
    "78 Pitampura Main Road, Delhi",
    "23 Shalimar Bagh Road, Delhi",
    "91 Punjabi Bagh Road, Delhi",
    "34 Rajouri Garden Road, Delhi",
    "56 Janakpuri Main Road, Delhi",
    "17 Dwarka Sector 10 Road, Delhi",
    "82 Uttam Nagar Road, Delhi",
    "29 Paschim Vihar Road, Delhi",
    "63 Lajpat Nagar Road, Delhi",
    "41 Greater Kailash Road, Delhi",
    "76 Saket Main Road, Delhi",
    "18 Malviya Nagar Road, Delhi",
    "52 Hauz Khas Road, Delhi",
    "37 Vasant Kunj Road, Delhi",
    "84 Mayur Vihar Road, Delhi",
    "25 Preet Vihar Road, Delhi",
    "69 Shahdara Main Road, Delhi",
    "31 Karol Bagh Road, Delhi"
]
state_address=['4','32','10','26']

indian_names= indian_female_names+indian_male_names
count =0
while count < 5:
    name=random.choice(indian_names)
    password=name.split(' ')[0]+'1234'.title()
    mobile = random.choice("6789") + ''.join(
        random.choices("0123456789", k=9)
    )
    email=(random.choice(name.split(' '))+''.join(random.choices(mobile, k=4))+"@gmail.com").lower()
    state=random.choice(state_address)
    street_address=''
    if state == '4':
        street_address=random.choice(bihar_addresses)
    elif state=='32':
        street_address=random.choice(delhi_addresses)
    elif state=='10':
        street_address=random.choice(jharkhand_addresses)
    elif state=='26':
        street_address=random.choice(uttar_pradesh_addresses)

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    #4=bihar,32=Delhi,10=jharkhand,26=uttar pardesh

    try:
        # Open registration page
        driver.get(
            "https://solarequitypay.com/joinus?_refertojoin=U0VQNTIyNDg2Mw=="
        )

        # Full name
        full_name = wait.until(
            EC.visibility_of_element_located((By.NAME, "full_name"))
        )
        full_name.send_keys(name)

        # Mobile
        driver.find_element(By.NAME, "mobile").send_keys(mobile)

        # Email
        driver.find_element(
            By.NAME, "email"
        ).send_keys(email)

        # State
        state_s = Select(
            driver.find_element(By.NAME, "state")
        )
        state_s.select_by_value(state)  

        # Address
        driver.find_element(
            By.NAME, "address"
        ).send_keys(street_address)

        # Password
        driver.find_element(
            By.NAME, "password"
        ).send_keys(password)

        # Confirm password
        driver.find_element(
            By.NAME, "confirm_password"
        ).send_keys(password)

        # CAPTCHA
        captcha_element = wait.until(
            EC.presence_of_element_located((By.NAME, "realCaptcha"))
        )

        captcha = captcha_element.get_attribute("value")

        driver.find_element(
            By.NAME, "userCaptcha"
        ).send_keys(str(captcha))



        submit = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "button[name='_btn_create']")
            )
        )

        # Scroll button into the visible area
        driver.execute_script("""
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center'
            });
        """, submit)

        # Save current URL before clicking
        old_url = driver.current_url

        # Try normal Selenium click first
        try:
            submit.click()

        except Exception:
            # Fallback if Selenium reports ElementClickInterceptedException
            driver.execute_script(
                "arguments[0].click();",
                submit
            )


        wait.until(
            EC.url_contains("/user/Welcome")
        )

        print("Registration successful!")
        print("Welcome URL:", driver.current_url)

        login_id = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//strong[contains(normalize-space(), 'Login ID:')]/following-sibling::span"
                )
            )
        ).text.strip()

        password_value = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//strong[contains(normalize-space(), 'Password:')]/following-sibling::span"
                )
            )
        ).text.strip()

        sponsor_id = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//strong[contains(normalize-space(), 'Sponsor ID:')]/following-sibling::span"
                )
            )
        ).text.strip()

        ok_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.swal2-confirm")
            )
        )

        ok_button.click()

        proceed_login = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[contains(normalize-space(), 'Proceed to Login')]"
                )
            )
        )

        proceed_login.click()

        wait.until(
            EC.url_contains("/Login")
        )

        print("Login page:", driver.current_url)
        # Wait for User ID field
        username_input = wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "username")
            )
        )

        # Enter Login ID
        username_input.send_keys(login_id)


        # Wait for Password field
        password_input = wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "userpass")
            )
        )

        # Enter Password
        password_input.send_keys(password_value)

        login_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[name='_btn_login']")
            )
        )

        login_button.click()

        wait.until(
            lambda d: "/user/Login" not in d.current_url
        )

        print("Login successful!")
        print("Dashboard URL:", driver.current_url)

        wait.until(
            EC.url_contains("/user/Dashboard")
        )

        print("Dashboard:", driver.current_url)

        print("Looking for Data Entry link...")

        data_entry = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@href, 'DataEntryTask')]")
            )
        )

        print("Data Entry link found!")
        print("Link:", data_entry.get_attribute("href"))

        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            data_entry
        )

        try:
            data_entry.click()
        except Exception:
            driver.execute_script(
                "arguments[0].click();",
                data_entry
            )

        wait.until(
            EC.url_contains("/user/DataEntryTask")
        )

        print("Data Entry page:", driver.current_url)

        rows = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "tbody tr[data-captcha]")
            )
        )

        print("Total rows:", len(rows))

        for index, row in enumerate(rows, start=1):

            # Get displayed data
            data_value = row.find_element(
                By.CSS_SELECTOR,
                "input.captcha-value"
            ).get_attribute("value").strip()

            # Find input box
            input_box = row.find_element(
                By.CSS_SELECTOR,
                "input.user-input"
            )

            # Fill the value
            input_box.clear()
            input_box.send_keys(data_value)

            print(f"Row {index}: {data_value} -> filled")

        wait.until(
            lambda d: all(
                row.find_element(
                    By.CSS_SELECTOR,
                    "input.user-input"
                ).get_attribute("value").strip() != ""
                for row in d.find_elements(
                    By.CSS_SELECTOR,
                    "tbody tr[data-captcha]"
                )
            )
        )

        print("All 10 rows are filled.")

        submit_button = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//button[contains(normalize-space(), 'Submit')]"
                )
            )
        )

        wait.until(
            lambda d: d.execute_script("""
                const el = arguments[0];
                const style = window.getComputedStyle(el);

                return style.display !== 'none'
                    && style.visibility !== 'hidden'
                    && el.offsetParent !== null;
            """, submit_button)
        )

        print("Submit button is visible.")

        driver.execute_script("""
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center'
            });
        """, submit_button)

        try:
            submit_button.click()

        except Exception:
            print("Normal click failed, using JavaScript click...")
            driver.execute_script(
                "arguments[0].click();",
                submit_button
            )
        # import time
        # time.sleep(3)
        count +=1

    except Exception as e:
        print("Error:", e)

    finally:
        pass