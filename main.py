from selenium_driverless.sync import webdriver
from selenium_driverless.types.by import By
from time import sleep
import re
import requests
from bs4 import BeautifulSoup


profile_directory = 'C:/Profile EMAIL-SCARPING'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--user-data-dir={profile_directory}')
chrome_options.add_argument('--headless=new')
driver = webdriver.Chrome(max_ws_size=2**50, options=chrome_options)
driver.set_single_proxy("http://ULdpEUe3yNcfojM5:4u1NN4VkgnKp17Ja_streaming-1@geo.iproyal.com:12321")

first_query = "usa"
niche = "influencer"
domain = "@gmail.com"
site = "instagram.com"

query = f"{first_query}+{niche}+@gmail.com+site:instagram.com"
driver.get(f"https://www.google.com/search?q={query}")
sleep(3)

while True:
    while True:
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            break
        except:
            pass


    soup = BeautifulSoup(driver.page_source, "html.parser")
    text = soup.get_text()

    # Step 3: Use regular expression to find email addresses
    # email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.com\b"
    emails = re.findall(email_pattern, text)

    # Step 4: Remove duplicates if needed
    unique_emails = list(set(emails))

    print("Extracted emails:", unique_emails)
    for email in unique_emails:
        with open('emails.txt', 'a', encoding='utf-8') as file:
            file.write(email + "\n")

    try:
        driver.find_element(By.CSS_SELECTOR, "a[id=\"pnnext\"]")
    except:
        break
    driver.execute_script(f'document.querySelector(\'a[id="pnnext"]\').click()')

    sleep(3)

driver.quit()