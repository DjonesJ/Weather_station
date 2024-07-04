from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


driver = webdriver.Firefox()
driver.get('https://www.dmi.dk/lokation/show/DK/2621213/Grevinge/')


# Click the accept button
a = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "coi-banner__accept")))
a = driver.find_element(By.CLASS_NAME, "coi-banner__accept")
a.click()

# Wait for homepage to load
wait = WebDriverWait(driver, 10)

for x in range(10):
    try:    
        b = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, f"//*[@id='{x}-accordionitem-day']/div/p[3]/span")))[0]
        lines = b.text.replace("°", "")
        numbers = re.split("/", lines)
        print(numbers[0].replace("°", ""))
        print(numbers[1].replace("°", ""))
        print("\n")
    except Exception as e:
        # Do some exception here and send the error message included in the email
        print(f"Failed to send email: {e}")



f = open("demofile2.txt", "a")
f.write(b.text)
f.close()


f = open("demofile2.txt", "r")


driver.close()