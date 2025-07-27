# 🛍️ Flipkart MacBook Price Scraper

This is a Python script that scrapes MacBook product names and prices from [Flipkart](https://www.flipkart.com/) using **ScraperAPI**.

## 📦 Features
- Scrapes product title and price from Flipkart
- Uses ScraperAPI to bypass bot protection
- Outputs clean `.xlsx` file using pandas

## 🖥️ Sample Output

| Product Name        | Price     |
|---------------------|-----------|
| Apple MacBook M4    | ₹1,19,900 |
| MacBook Pro M4 Max  | ₹2,49,900 |

See the file: `products.xlsx`

## 📸 Screenshots

### Terminal:
![Terminal]([screenshots/terminal_run.png](https://github.com/SaurabhKr88/flipkart-price-tracker/blob/b0d6a3b547f2f5bcc432a04edcd26ba04e100ef4/screenshot.jpeg))

### Excel Output:
![Excel](macbook_prices.xlsx)

## 🔧 Requirements

- Python 3
- pandas
- requests

Install with:
```bash
pip install -r requirements.txt
