import re
import json

# 🔹 Step 1: Read the txt file
with open("markdown.txt", "r", encoding="utf-8") as file:
    markdown = file.read()

# 🔹 Step 2: Extract data using regex
pattern = re.findall(
    r'### \[(.*?)\].*?£(\d+\.\d+).*?(In stock|Out of stock)',
    markdown,
    re.DOTALL
)

# Extract titles
titles = re.findall(r'### \[(.*?)\]', markdown)

# Extract prices
prices = re.findall(r'£(\d+\.\d+)', markdown)

# Extract stock status
stocks = re.findall(r'(In stock|Out of stock)', markdown)

# Combine into structured data
books = []
for i in range(min(len(titles), len(prices), len(stocks))):
    books.append({
        "title": titles[i],
        "price": float(prices[i]),
        "stock": stocks[i]
    })

# Print clean JSON
print(json.dumps(books, indent=2))