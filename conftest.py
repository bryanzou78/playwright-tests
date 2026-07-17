import pytest

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {**browser_type_launch_args, "slow_mo": 1000}

@pytest.fixture
def page_on_wiki_homepage(page):
    page.goto('https://www.wikipedia.org')
    yield page

@pytest.fixture
def page_on_einstein_article(page):
    page.goto('https://en.wikipedia.org/wiki/Albert_Einstein')
    yield page

@pytest.fixture
def search(page_on_wiki_homepage):
    def run(term):
        page_on_wiki_homepage.locator('input#searchInput').click()
        page_on_wiki_homepage.locator('input#searchInput').fill(term)
        page_on_wiki_homepage.keyboard.press('Enter') 
    yield run
        