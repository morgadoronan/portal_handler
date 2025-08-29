from navigation.navigator import Navigator
from scraping.table_scraper import TableScraper
from repository.sqlite_repository import SQLiteRepository
from models.metadata import Metadata

def main():
    # Initialize the navigator
    navigator = Navigator()
    
    # Navigate to the target URL
    url = "https://docs.python.org/3/download.html"  # Replace with the actual URL
    page = navigator.navigate(url)
    
    # Initialize the table scraper
    table_scraper = TableScraper()
    
    # Scrape the first table found on the page
    metadata = table_scraper.scrape_table(page)
    
    # Initialize the SQLite repository
    repository = SQLiteRepository()
    
    # Save the scraped metadata to the database
    repository.save_record(metadata)

if __name__ == "__main__":
    main()