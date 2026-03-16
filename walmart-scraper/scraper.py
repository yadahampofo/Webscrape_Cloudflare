import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def get_trending_walmart():
    url = "https://www.walmart.com/search?q=trending&sort=best_seller"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Spoof a real browser to avoid blocks
        await page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        
        await page.goto(url, wait_until="networkidle")
        await page.wait_for_timeout(3000)  # let badges render
        
        html = await page.content()
        await browser.close()

    soup = BeautifulSoup(html, "html.parser")
    results = []

    # Each product is in an article tag
    for card in soup.find_all("div", {"data-item-id": True}):
        badge = card.find(string=lambda t: t and "bought since yesterday" in t.lower())
        if badge:
            name = card.find("span", {"data-automation-id": "product-title"})
            price = card.find("div", {"itemprop": "price"})
            results.append({
                "name": name.text.strip() if name else "N/A",
                "price": price.text.strip() if price else "N/A",
                "badge": badge.strip()
            })

        if len(results) >= 10:
            break

    for i, item in enumerate(results, 1):
        print(f"{i}. {item['name']} | {item['price']} | {item['badge']}")

asyncio.run(get_trending_walmart())