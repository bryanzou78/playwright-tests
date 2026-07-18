import requests

def test_title_matches_api(page, page_on_einstein_article):
    headers = {'User-Agent': 'playwright-tests portfolio (https://github.com/bryanzou78)'}
    response = requests.get('https://en.wikipedia.org/api/rest_v1/page/summary/Albert_Einstein', headers=headers)
    assert response.status_code == 200
    data = response.json()
    
    api_title = data['title']
    rendered_title = page.locator('#firstHeading').text_content()

    assert api_title == rendered_title