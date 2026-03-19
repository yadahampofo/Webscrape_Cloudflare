# 🚀 Real-Time Web Crawling Pipeline with Cloudflare Browser Rendering API

## 📌 Overview
This project explores **real-time web data extraction** using Cloudflare’s newly released **Browser Rendering Crawl Endpoint**.

The goal was to move beyond static scraping and experiment with a **modern, API-driven crawling workflow** that can render JavaScript-heavy pages and return structured content for downstream processing.

---

## ⚡ What This Project Demonstrates
- Early adoption of **newly released APIs**
- Working with **Cloudflare Browser Rendering infrastructure**
- Building a **crawl → parse → structure pipeline**
- Handling **unstructured markdown output** and converting it into usable data
- Practical experience with **real-world scraping challenges**

---

## 🔧 Tech Stack

- **Python 3**
- **Cloudflare Browser Rendering API**
- **Regex-based parsing**
- **JSON data structuring**

---

## 📡 API Used

**Endpoint:**
- POST /accounts/{account_id}/browser-rendering/crawl

  
**Features explored:**
- Page rendering (`"render": true`)
- Markdown extraction
- Crawl job execution and response handling

---

## 🧠 Key Learnings

### 1. Crawling ≠ Extraction
The API successfully retrieves content, but:

> The real challenge is transforming noisy, unstructured output into clean data.

---

### 2. Markdown vs HTML Tradeoffs
- Markdown is lightweight but messy for parsing  
- HTML retains structure and is better suited for production-grade pipelines  

---

### 3. Real-World Scraping Challenges
- Inconsistent formatting across pages  
- Navigation and UI noise in extracted content  
- Data alignment issues (titles vs prices vs stock)  

---

## 🚀 Future Improvements

- Transition to **HTML parsing (BeautifulSoup / Cheerio)** for improved reliability  
- Implement **pagination crawling** (50+ pages)  
- Store structured data in a **database (PostgreSQL / MongoDB)**  
- Build a **real-time ingestion pipeline**  
- Add **deduplication, validation, and monitoring layers**  
