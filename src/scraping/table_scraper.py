from src.interfaces.abstract_scraper import AbstractScraper


class TableScraper(AbstractScraper):
    def __init__(self):
        pass

    async def scrape_table(self, page):
        table = await page.query_selector('table')
        if not table:
            raise ValueError("No table found on the page.")

        rows = await table.query_selector_all('tr')
        metadata = []

        for row in rows:
            columns = await row.query_selector_all('td')
            if columns:
                column_data = [await column.inner_text() for column in columns]
                metadata.append(column_data)

        return self.transform_metadata(metadata)

    def transform_metadata(self, raw_data):
        # Transform raw data into structured metadata
        # This method should be overridden in subclasses if needed
        return raw_data