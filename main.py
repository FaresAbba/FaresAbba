from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from fake_useragent import UserAgent
import time
import csv

options = Options()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option(
    "prefs", {"profile.managed_default_content_settings.media_stream": 2}
)
options.add_argument("--start-maximized")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920,1200")
options.add_argument("--mute-audio")
options.add_argument("--blink-settings=imagesEnabled=false")
options.add_argument("--disable-notifications")
options.add_argument("--disable-features=PreloadMediaEngagementData,MediaEngagementBypassAutoplayPolicies")
options.add_argument("--autoplay-policy=user-required")
ua = UserAgent()
options.add_argument(f"user-agent={ua.random}")

monpilote = webdriver.Chrome(options=options)
print("Chrome démarré")

a = [["Film", "Note"]]

for page in range(1, 4):
    url = f"https://www.allocine.fr/film/meilleurs/?page={page}"
    monpilote.get(url)
    time.sleep(8)

    films = monpilote.find_elements(By.CSS_SELECTOR, 'a.meta-title-link')
    notes = monpilote.find_elements(By.CSS_SELECTOR, 'span.stareval-note')

    print(f"Page {page} — Films : {len(films)} | Notes : {len(notes)}")

    for i in range(min(len(films), len(notes))):
        film = films[i].text.strip()
        note = notes[i].text.strip()
        if film:
            if note == "--":
                note = "N/A"
            a.append([film, note])
            print(film, note)

with open("AlloCine.csv", "w", newline="", encoding="utf-8") as f:
    ecrivain = csv.writer(f, delimiter=",")
    ecrivain.writerows(a)

print(f"AlloCine.csv généré avec {len(a)-1} films !")
monpilote.quit()