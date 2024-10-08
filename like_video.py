import time
import random
import sys
import threading
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from fake_useragent import UserAgent
import undetected_chromedriver as uc
from utils.terminal.print_manager import print_colored_text
from utils.database.database_manager import execute_sql_query, get_proxies_by_country
from utils.files.files_manager import get_proxies_from_file


class RumbleLiker:
    def __init__(self, amount_of_bots, start_count, video_url, server_hub="your_server_ip"):
        self.amount_of_bots = int(amount_of_bots)
        self.start_count = int(start_count)
        self.video_url = video_url
        self.server_hub = server_hub
        # From Database
        #self.proxies = get_proxies_by_country("ALL")
        # Local
        self.proxies = get_proxies_from_file()

    def print_and_log(self, text, account, i, error=False):
        progress = f"[ {i + 1} | {self.amount_of_bots} ]"
        message = f"{progress} - [{account}] {text}"
        if error:
            print_colored_text("RUMBLE LIKES", message, "RED")
        else:
            print_colored_text("RUMBLE LIKES", message, "GREEN")

    def like_rumble_video(self, driver, accountname, password, i):
        time.sleep(3)
        try:
            login_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Sign In')]"))
            )
            driver.execute_script("arguments[0].click();", login_button)
            time.sleep(3)
            action = ActionChains(driver)
            action.send_keys(accountname).send_keys(Keys.TAB).perform()
            time.sleep(1)
            action.send_keys(password).send_keys(Keys.TAB).send_keys(Keys.TAB).perform()
            action.send_keys(Keys.ENTER).perform()
            try:
                time.sleep(3)
                like_button = WebDriverWait(driver, 3).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, '.rumbles-vote-pill-up'))
                )
                time.sleep(2)
                driver.execute_script("arguments[0].click();", like_button)
                self.print_and_log("SUCCESSFULLY LIKED", accountname, i)
                time.sleep(3)
                driver.quit()
            except Exception:
                try:
                    like_button = WebDriverWait(driver, 3).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-js="rumble_vote_up"]'))
                    )
                    time.sleep(2)
                    driver.execute_script("arguments[0].click();", like_button)
                    self.print_and_log("SUCCESSFULLY LIKED", accountname, i)
                    driver.quit()
                except:
                    self.print_and_log("ALREADY LIKED", accountname, i, error=True)
                    driver.delete_all_cookies()
                    driver.quit()
        except Exception:
            driver.delete_all_cookies()
            driver.quit()

    def like_rumble_channel(self, i):
        try:
            query = f"SELECT * FROM `rumble` WHERE `id` = {i + self.start_count}"
            account_result = execute_sql_query("bots", query)
            account = account_result[0]['accountName']
            password = account_result[0]['password']

            options = uc.ChromeOptions()
            ua = UserAgent()
            random_user = ua.random
            proxy = random.choice(self.proxies)
            options.add_argument(f"user-agent={random_user}")
            options.add_argument(f'--proxy-server={proxy}')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_argument("--allow-running-insecure-content")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-web-security")
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")

            prefs = {"profile.managed_default_content_settings.images": 1}
            options.add_experimental_option("prefs", prefs)
            driver = webdriver.Remote(command_executor=f'http://{self.server_hub}:4444', options=options)
            time.sleep(1)
            driver.get(self.video_url)
            self.like_rumble_video(driver, account, password, i)
        except Exception as e:
            self.print_and_log("ERROR LIKING VIDEO!", account, i, error=True)
            driver.quit()

    def start_bots(self):
        self.print_and_log(f"STARTED {self.amount_of_bots} LIKES FOR {self.video_url.upper()}", "INFO", 0)
        threads = []
        for i in range(self.amount_of_bots):
            thread = threading.Thread(target=self.like_rumble_channel, args=(i,))
            thread.start()
            time.sleep(random.randint(2, 5))
            threads.append(thread)
        for thread in threads:
            thread.join()
        self.print_and_log(f"FINISHED {self.amount_of_bots} LIKES FOR {self.video_url.upper()}", "", self.amount_of_bots, error=False)

    def start_rumble_likes(self):
        self.start_bots()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 like_video.py <amount_of_bots> <start_count> <video_url>")
        sys.exit(1)
    amount_of_bots, start_count, video_url = sys.argv[1], sys.argv[2], sys.argv[3]
    liker = RumbleLiker(amount_of_bots, start_count, video_url)
    liker.start_rumble_likes()
