from playwright.sync_api import expect

def test_homepage_loads(page):
    page.goto('https://www.wikipedia.org')
    expect(page).to_have_title('Wikipedia')

def test_search_navigates_to_correct_article(page):
    page.goto('https://www.wikipedia.org')
    page.locator('input#searchInput').click()
    page.locator('input#searchInput').fill('Albert Einstein')
    page.keyboard.press('Enter')
    expect(page.locator('h1')).to_contain_text('Albert Einstein')

def test_clicking_link_navigates_to_article(page):
    page.goto('https://en.wikipedia.org/wiki/Albert_Einstein')
    page.locator("a[title='Theoretical physicist']").click()
    expect(page.locator('#firstHeading')).to_contain_text('Theoretical physics')

def test_article_has_expected_section(page):
    page.goto('https://en.wikipedia.org/wiki/Albert_Einstein')
    expect(page.locator('#Life_and_career')).to_be_visible()