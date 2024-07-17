# webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from datetime import timedelta
# Automatic mail
import smtplib, ssl
from email.mime.text import MIMEText
import time

 

from constants import sender_email, password, receiver_email


def getData():
    temp_list_max = []
    temp_list_min = []

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.dmi.dk/lokation/show/DK/2621213/Grevinge/')

 

    # Click the accept button
    a = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "coi-banner__accept")))
    a = driver.find_element(By.CLASS_NAME, "coi-banner__accept")
    a.click()

    counter = 0
    date_array = []

    for x in range(10):
        try:   
            b = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, f"//*[@id='{x}-accordionitem-day']/div/p[3]/span")))[0]
            date_string = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, f"//*[@id='{x}-accordionitem-day']/div/p[1]/span[1]")))
            for x in date_string:
                date_array.append(x.text.replace("\n", ""))
            lines = b.text.replace("°", "")
            numbers = re.split("/", lines)
            temp_list_max.append(numbers[0].replace("°", ""))
            temp_list_min.append(numbers[1].replace("°", ""))
            counter = counter + 1
            
        except Exception as e:
            # Do some exception here and send the error message included in the email
            print(f"Failed to obtain weather data from homepage: {e}")

    count = 0
    text = ""
    for x in date_array:
        if(int(temp_list_max[count]) > 22):
            text += date_array[count]
            text += "Temp is: " + temp_list_max[count] + "\n"
        count = count + 1
    print(text)
    # save data as a text file (perhaps for future use)
    f = open("demofile2.txt", "a")
    f.write(text)
    f.close()
    f = open("demofile2.txt", "r")

    driver.close()
    return text

def sendMail(text):
    port = 587
    smtp_server = "smtp.gmail.com"
    message = MIMEText(text, "plain")
    message["subject"] = "Grevinge winter weather updates"
    message["From"] = sender_email
    message["To"] = receiver_email

 

    context = ssl.create_default_context()

 

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email send successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

    '''
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email1, message)
        print("Email send successfully")
    '''



if __name__=="__main__": 
    while(True):
        # It is not ideal to let an applicatin sleep, instead we should let the processor do other tasks
        # but since this is the only task that this application are performing at the moment, then this is fine
        # for now. But maybe we should create a Cron tab instead, maybe that will come later.
        
        text = getData()
        
        sendMail(text)
        #time.sleep(86400)
        time.sleep(10)