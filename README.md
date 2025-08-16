# Nature.com Web Scraper

A Python web scraper designed to extract articles from Nature.com based on publication date and article type.

## Description

This scraper allows you to download articles from Nature.com's archives, organizing them by page number and filtering by article type. It extracts article titles and teasers, saving them as text files in organized directories.

## Features

- **Date-based Scraping**: Scrapes articles from Nature.com sorted by publication date (currently set to 2020)
- **Article Type Filtering**: Filters articles by type (e.g., research articles, news, reviews)
- **Automatic Organization**: Creates directories for each page and saves articles as text files
- **Title Sanitization**: Removes punctuation and spaces from article titles for clean file names
- **HTTP Status Checking**: Validates URLs before processing

## Requirements

```python
beautifulsoup4
requests
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/nature-webscraper.git
cd nature-webscraper
```

2. Install required dependencies:
```bash
pip install beautifulsoup4 requests
```

## Usage

1. Run the scraper:
```bash
python scraper.py
```

2. When prompted, enter:
   - **Number of pages**: How many pages to scrape (e.g., `5`)
   - **Article type**: The type of articles to filter (e.g., `Article`, `News`, `Review`)

3. The scraper will:
   - Create directories named `Page_1`, `Page_2`, etc.
   - Save article content as `.txt` files in respective directories
   - Display "Saved all articles" when complete

## Output Structure

```
project-directory/
├── scraper.py
├── Page_1/
│   ├── Article_Title_1.txt
│   ├── Article_Title_2.txt
│   └── ...
├── Page_2/
│   ├── Article_Title_3.txt
│   └── ...
└── ...
```

## Code Structure

### Main Functions

- `get_url_status(url)`: Checks HTTP status of URLs
- `write_html(url)`: Retrieves HTML content from URLs
- `get_link_write_news(link)`: Extracts and saves individual articles

### Process Flow

1. User inputs number of pages and article type
2. For each page:
   - Constructs URL with page number
   - Parses HTML content
   - Filters articles by specified type
   - Creates page directory
   - Downloads and saves articles
   - Returns to base directory

## Configuration

The scraper is currently configured to:
- Scrape from Nature.com articles published in 2020
- Use English language preference
- Sort articles by publication date

To modify the year or other parameters, edit the `url` variable in `scraper.py`:
```python
url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page="
```


This project is provided as-is for educational purposes. Please respect Nature.com's terms of service and robots.txt when using this scraper.

## Disclaimer

This tool is for educational and research purposes only. Users are responsible for complying with Nature.com's terms of service and applicable laws regarding web scraping.
