from playwright.sync_api import expect

def test_homepage_loads(page):
    page.goto('https://www.wikipedia.org')
    expect(page).to_have_title('Wikipedia')

def test_search_goes_to_correct_article(page):
    page.goto('https://www.wikipedia.org')
    page.locator('input#searchInput').click()
    page.locator('input#searchInput').fill('Albert Einstein')
    page.keyboard.press('Enter')
    expect(page.locator('h1')).to_contain_text('Albert Einstein')