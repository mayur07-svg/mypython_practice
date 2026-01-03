from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# -----------------------------
# List of specific contacts
specific_contacts = ["+919660930066", "+918003636852", "+919328396539"]

# Message and poster
message = "Hello! Check out this poster."
# Image in same folder as script
image_path = os.path.abspath("rename.png")
# -----------------------------

# Start Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.whatsapp.com")
print("Please scan the QR code if not already logged in...")
time.sleep(20)  # Wait time to scan QR code manually

for contact in specific_contacts:
    # Search for contact
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.clear()
    search_box.send_keys(contact)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

    # Click attach button
    attach_btn = driver.find_element(By.XPATH, '//span[@data-icon="clip"]')
    attach_btn.click()
    time.sleep(1)

    # Upload image
    image_input = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_input.send_keys(image_path)
    time.sleep(2)

    # Add caption
    caption_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]')
    caption_box.send_keys(message)
    time.sleep(1)

    # Send image + message
    send_btn = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
    send_btn.click()
    time.sleep(3)  # Wait before next contact

print("All messages sent successfully!")
driver.quit()
