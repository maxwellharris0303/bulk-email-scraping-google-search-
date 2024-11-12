from selenium_driverless.sync import webdriver
from selenium_driverless.types.by import By
from time import sleep
import re
import requests
from bs4 import BeautifulSoup
import threading

# Initialize a lock for the critical section
lock = threading.Lock()
email_file_lock = threading.Lock()


# profile_directory = 'C:/Profile EMAIL-SCARPING-2'
# chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument(f'--user-data-dir={profile_directory}')
# chrome_options.add_argument('--blink-settings=imagesEnabled=false')
# chrome_options.add_argument('--headless=new')


def run(us_cities, index):
    with lock:
        with open("niches.txt", 'r', encoding='utf-8') as file:
            lines = file.readlines()
        niches = [line.strip().replace(" ", "+") for line in lines]

        with open("domains.txt", 'r', encoding='utf-8') as file:
            lines = file.readlines()
        domains = [line.strip().replace(" ", "+") for line in lines]

        with open("sites.txt", 'r', encoding='utf-8') as file:
            lines = file.readlines()
        sites = [line.strip().replace(" ", "+") for line in lines]

    first_queries = us_cities

    for first_query in first_queries:
        with lock:
            with open("progress.txt", 'a', encoding='utf-8') as file:
                file.write(first_query + "\n")
        for niche in niches:
            for domain in domains:
                for site in sites:
                    try:
                        chrome_options = webdriver.ChromeOptions()
                        # chrome_options.add_argument(f'--user-data-dir={profile_directory}')
                        chrome_options.add_argument('--blink-settings=imagesEnabled=false')
                        chrome_options.add_argument('--headless=new')
                        driver = webdriver.Chrome(max_ws_size=2**50, options=chrome_options)
                        # driver.set_single_proxy("http://ULdpEUe3yNcfojM5:4u1NN4VkgnKp17Ja_streaming-1@geo.iproyal.com:12321")
                        # driver.set_single_proxy("0a84b9db1cab2b518657__cr.us:9d43141d1ed58228@gw.dataimpulse.com:823")

                        # driver.execute_cdp_cmd('Network.enable', {})
                        # driver.execute_cdp_cmd('Network.setBlockedURLs', {"urls": ["*.css", "*.js", "*.png", "*.jpg", "*.gif", "*.svg"]})
                        _first_query = first_query
                        _niche = niche
                        _domain = domain
                        _site = site

                        query = f"{_first_query}+{_niche}+{_domain}+site:{_site}"
                        driver.get(f"https://www.bing.com/search?q={query}", wait_load=True)
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
                            with email_file_lock:
                                for email in unique_emails:
                                    with open(f'emails{index}.txt', 'a', encoding='utf-8') as file:
                                        file.write(email + "\n")
                            try:
                                # driver.find_element(By.CSS_SELECTOR, "a[id=\"pnnext\"]")
                                driver.find_element(By.CSS_SELECTOR, "a[class=\"sb_pagN sb_pagN_bp b_widePag sb_bp \"]")
                            except:
                                break
                            # driver.execute_script(f'document.querySelector(\'a[id="pnnext"]\').click()')
                            driver.execute_script(f'document.querySelector(\'a[class="sb_pagN sb_pagN_bp b_widePag sb_bp "]\').click()')

                            sleep(3)
                        
                        driver.quit()
                    except:
                        try:
                            driver.quit()
                        except:
                            pass