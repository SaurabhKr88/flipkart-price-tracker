from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

def scrape_flipkart_macbooks():
    # Setup Chrome with Selenium
    options = Options()
    # options.add_argument("--headless")  # Uncomment this line to run in background
    driver = webdriver.Chrome(options=options)

    try:
        url = "https://www.flipkart.com/search?q=macbook"
        driver.get(url)
        time.sleep(3)  # Let the page load

        # Close login popup if it appears
        try:
            close_button = driver.find_element(By.XPATH, '//button[text()="✕"]')
            close_button.click()
            time.sleep(1)
        except Exception:
            pass  # No popup, continue

        # Extract product names and prices
        names = driver.find_elements(By.CSS_SELECTOR, "div.KzDlHZ")
        prices = driver.find_elements(By.CSS_SELECTOR, "div.Nx9bqj._4b5DiR")

        # Build data list
        products = []
        for name, price in zip(names, prices):
            products.append({
                "Product Name": name.text.strip(),
                "Price": price.text.strip()
            })

        # Convert to DataFrame and export to Excel
        df = pd.DataFrame(products)
        df.to_excel("macbook_prices.xlsx", index=False)
        print("✅ Scraping completed. Data saved to macbook_prices.xlsx")

    except Exception as e:
        print("❌ An error occurred:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_flipkart_macbooks()
