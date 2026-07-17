from playwright.sync_api import expect

def test_homepage_loads(page,page_on_wiki_homepage):
    expect(page).to_have_title('Wikipedia')

def test_search_navigates_to_correct_article(page, page_on_wiki_homepage):
    page.locator('input#searchInput').click()
    page.locator('input#searchInput').fill('Albert Einstein')
    page.keyboard.press('Enter')
    expect(page.locator('h1')).to_contain_text('Albert Einstein')

def test_clicking_link_navigates_to_article(page, page_on_einstein_article):
    page.locator("a[title='Theoretical physicist']").click()
    expect(page.locator('#firstHeading')).to_contain_text('Theoretical physics')

def test_article_has_expected_section(page, page_on_einstein_article):
    expect(page.locator('#Life_and_career')).to_be_visible()

def test_search_no_results(page, search):
    search('xyz123nonsense')
    expect(page.locator('.mw-search-nonefound')).to_contain_text('There were no results matching the query.')
