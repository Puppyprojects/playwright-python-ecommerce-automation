from playwright.sync_api import Page


class BasePage:
    """Common behaviour shared by every page object."""

    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str = "/"):
        self.page.goto(path)

    @property
    def title(self) -> str:
        return self.page.title()

    @property
    def url(self) -> str:
        return self.page.url
