from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime
import time

# --- CONFIG ---
PRODUCT_URL = "https://www.flipkart.com/poco-m6-pro-5g-forest-green-128-gb/p/itm36920f23ff9b4"
EXCEL_FILE = "flipkart_price_log.xlsx"

# --- SETUP ---
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # comment this out if you want to see the browser
driver = webdriver.Chrome(options=options)

# --- SCRAPE ---
driver.get(PRODUCT_URL)
time.sleep(5)  # wait for JS to load

try:
    price = driver.find_element(By.CLASS_NAME, "_30jeq3").text
    product_title = driver.find_element(By.CLASS_NAME, "B_NuCI").text
except:
    print("Error: Price or product not found")
    driver.quit()
    exit()

# --- CLEAN DATA ---
price = price.replace("₹", "").replace(",", "").strip()
price_int = int(price)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --- SAVE TO EXCEL ---
data = {
    "Timestamp": [timestamp],
    "Product": [product_title],
    "Price (INR)": [price_int]
}

try:
    df_existing = pd.read_excel(EXCEL_FILE)
    df_new = pd.DataFrame(data)
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
except FileNotFoundError:
    df_combined = pd.DataFrame(data)

df_combined.to_excel(EXCEL_FILE, index=False)
print(f"Logged {product_title} at ₹{price_int}")

driver.quit()
