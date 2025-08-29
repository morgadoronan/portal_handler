class Navigator:
    def __init__(self, browser):
        self.browser = browser

    async def navigate(self, url):
        page = await self.browser.new_page()
        await page.goto(url)
        return page

    async def close(self, page):
        await page.close()