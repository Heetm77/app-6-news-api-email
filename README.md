# app-6-news-api-email

Fetches the latest news articles for a chosen topic from NewsAPI and (optionally) prepares them to be sent via email. The current script downloads and prints article titles and descriptions; you can extend it to deliver the results through your preferred mail provider.

## Features
- Queries NewsAPI for recent articles on a configurable topic and date range.
- Prints article titles and descriptions to stdout for quick review.
- Simple, dependency-light Python script (only requires `requests`).

## Prerequisites
- Python 3.8+
- A NewsAPI key (sign up at https://newsapi.org/)

## Setup
1. Install dependencies:
   ```bash
   pip install requests
   ```
2. Create an environment variable for your API key:
   ```bash
   export NEWS_API_KEY=YOUR_KEY_HERE
   ```
   On Windows (PowerShell):
   ```powershell
   $env:NEWS_API_KEY="YOUR_KEY_HERE"
   ```

## Configuration
The current script (`main.py`) hardcodes the query, date, and API key. For production use, update these to read from environment variables:
- `NEWS_API_KEY` – your NewsAPI key (required)
- `NEWS_QUERY` – search term, e.g., `tesla` (default in script)
- `NEWS_FROM_DATE` – ISO date string, e.g., `2024-12-05`

Example pattern you can adapt inside `main.py`:
```python
import os
API_KEY = os.environ["NEWS_API_KEY"]
QUERY = os.getenv("NEWS_QUERY", "tesla")
FROM_DATE = os.getenv("NEWS_FROM_DATE", "2024-12-05")
```

## Running
```bash
python main.py
```
You’ll see article titles and descriptions printed to the console.

## Extending to email
- Add SMTP credentials (or a service like SendGrid/Mailgun/AWS SES).
- Format the fetched articles into plain text or HTML.
- Send the compiled body to your recipient list.

## Notes
- Keep your API key private; never commit it to version control.
- NewsAPI free tier has request and source restrictions—review their pricing/limits before deploying.