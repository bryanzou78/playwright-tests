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