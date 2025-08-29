from abc import ABC, abstractmethod

class AbstractScraper(ABC):
    @abstractmethod
    def scrape(self, url):
        pass

    @abstractmethod
    def transform_metadata(self, raw_data):
        pass