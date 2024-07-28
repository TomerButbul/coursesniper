import time
import pymysql
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException

# Path to ChromeDriver
PATH = r"C:\Program Files (x86)\chromedriver-win64\chromedriver.exe"
service = Service(PATH)

# Chrome options to ignore SSL errors and detach browser
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_experimental_option("detach", True)

# Initialize the Chrome driver with the service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Tomcar123!',
    'database': 'coursesniper'
}

# Function to retrieve active class codes from the database
def get_class_codes():
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT course_code FROM snipes WHERE status = 'active'")
            class_codes = [row[0] for row in cursor.fetchall()]
    finally:
        connection.close()
    return class_codes

# Function to log in to the portal
def login():
    # Open the login page
    driver.get("https://wl.mypurdue.purdue.edu/web/portal/registration")

    # Wait for the username field and enter the username
    user = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    user.send_keys("cbutbul")
    user.send_keys(Keys.RETURN)

    # Wait for the password field and enter the password
    password = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password.send_keys("Butbc001.310")
    password.send_keys(Keys.RETURN)

    # Wait 15 seconds after login (adjust as needed)
    time.sleep(15)

    # Navigate to the timetable page
    driver.get("https://timetable.mypurdue.purdue.edu/Timetabling/gwt.jsp?page=sectioning#0")

    # Wait 10 seconds on the timetable page (adjust as needed)
    time.sleep(10)

    # Click on <div class="gwt-Label">Fall</div>
    fall_div = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='gwt-Label' and text()='Fall']"))
    )
    fall_div.click()

    # Wait for some time after clicking "Fall" (optional)
    time.sleep(5)

    # Click on "New Course" button
    new_course_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@title='Add a new course to the schedule or drop an existing course from the schedule without going back to the Course Requests.']"))
    )
    new_course_button.click()

# Function to fetch course details and handle stale element exceptions
def fetch_course_details(class_code):
    try:
        # Wait for the search input and enter the course code
        search_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[1]/td/div/div[2]/input"))
        )
        search_input.clear()  # Clear the input field before entering new class code
        search_input.send_keys(class_code)
        time.sleep(1)  # Add a small delay to avoid race conditions
        
        # Wait for the Subject, Course, and Avail elements to be present
        subject = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/div/div[1]/div/table/tbody/tr[2]/td[1]/div"))
        )
        course = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/div/div[1]/div/table/tbody/tr[2]/td[2]/div"))
        )
        avail = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td/div/div[1]/div/table/tbody/tr[2]/td[3]/div"))
        )
        
        # Extract the text content of "Avail" and convert to integers
        available, total = map(int, avail.text.split('/'))
        current_avail = available
        
        return subject.text, course.text, current_avail
    
    except StaleElementReferenceException:
        print(f"StaleElementReferenceException occurred while fetching course details for class code {class_code}. Retrying...")
        return None, None, None
    except ValueError:
        print(f"ValueError occurred while converting availability to integers for class code {class_code}.")
        return None, None, None

# Store previous availability statuses
previous_availabilities = {}

try:
    login()

    while True:
        # Retrieve class codes from the database
        class_codes = get_class_codes()
        for class_code in class_codes:
            subject, course, current_avail = fetch_course_details(class_code)
            if subject is None or course is None or current_avail is None:
                continue
            
            # Check if the class has a spot open
            if current_avail > 0:
                print(f"Class {class_code} has a spot open! Subject: {subject}, Course: {course}, Avail: {current_avail}")
            
            # Print the values only if the availability has changed
            if class_code not in previous_availabilities or previous_availabilities[class_code] != current_avail:
                print(f"Subject: {subject}, Course: {course}, Avail: {current_avail}")
                previous_availabilities[class_code] = current_avail
            
            time.sleep(5)

        # Wait for a while before checking the database again
        time.sleep(5)

except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
    print(f"Exception occurred: {e}")

finally:
    # Close the browser
    driver.quit()
