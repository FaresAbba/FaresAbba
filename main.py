from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time

options = Options()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920,1200")
options.add_argument("--disable-notifications")
ua = UserAgent()
options.add_argument(f"user-agent={ua.random}")

monpilote = webdriver.Chrome(options=options)
print("Chrome démarré")

monpilote.get("https://fr.aliexpress.com/wholesale?SearchText=veste")
time.sleep(15)

print(monpilote.title)
print(monpilote.current_url)

h3 = monpilote.find_elements(By.TAG_NAME, 'h3')
print(f"h3 trouvés : {len(h3)}")
for el in h3[:5]:
    print(el.text)

time.sleep(20)
monpilote.execute_script("window.scrollTo(0, 1000);")
time.sleep(5)

spans = monpilote.find_elements(By.CSS_SELECTOR, 'span[class*="title"]')
print(f"spans titre : {len(spans)}")
for el in spans[:5]:
    print(el.text)

prix = monpilote.find_elements(By.CSS_SELECTOR, 'span[class*="price"]')
print(f"spans prix : {len(prix)}")
for el in prix[:5]:
    print(el.text)