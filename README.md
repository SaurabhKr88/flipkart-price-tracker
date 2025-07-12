# flipkart-price-tracker
# Flipkart Price Tracker (Prototype)

This Python script monitors the price of a product on Flipkart and logs it to an Excel file. Useful for tracking price drops on electronics or seasonal sales.

## 🔧 Tech Used
- Python
- Selenium (for browser automation)
- pandas + openpyxl (for Excel output)
- datetime / time (for timestamp and delay)

## 🚀 How It Works
- Loads the product page using Selenium
- Scrapes the product name and current price
- Writes it to an Excel file with timestamp
- Can be scheduled to run daily

## 📁 Output Sample
| Timestamp | Product | Price (INR) |
|-----------|---------|-------------|
| 2025-07-10 20:31 | POCO M6 Pro | 9999 |

## 🔗 How to Run
```bash
pip install selenium pandas openpyxl
python flipkart_tracker.py
