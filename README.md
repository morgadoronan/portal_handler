# Portal Handler

Portal Handler is a Python project designed to navigate websites and scrape data from tables, transforming the columns into structured metadata. This project utilizes Playwright for web navigation and scraping, and it implements a repository pattern for data access using SQLite.

## Project Structure

```
portal_handler
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── navigation
│   │   ├── __init__.py
│   │   └── navigator.py
│   ├── scraping
│   │   ├── __init__.py
│   │   └── table_scraper.py
│   ├── repository
│   │   ├── __init__.py
│   │   └── sqlite_repository.py
│   ├── interfaces
│   │   ├── __init__.py
│   │   └── abstract_scraper.py
│   └── models
│       ├── __init__.py
│       └── metadata.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

To get started with Portal Handler, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd portal_handler
pip install -r requirements.txt
```

## Usage

To run the application, execute the following command:

```bash
python src/main.py
```

## Components

- **Navigator**: Responsible for navigating to specified URLs and interacting with web pages.
- **TableScraper**: Finds and scrapes the first table on a webpage, transforming its columns into metadata.
- **SQLiteRepository**: Implements data access methods for saving and fetching records from a SQLite database.
- **AbstractScraper**: Defines the main functions for scraping, allowing for the creation of derivatives for other websites.
- **Metadata**: Represents the structure of the metadata extracted from the scraped table.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
