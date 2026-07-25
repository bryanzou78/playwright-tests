# playwright-tests

![CI](https://github.com/bryanzou78/playwright-tests/actions/workflows/tests.yml/badge.svg)

Browser automation tests for [Wikipedia](https://www.wikipedia.org) using Python and Playwright.

Built as a standalone testing project targeting a live third-party site, demonstrating the ability to write browser tests against an unfamiliar product. Where [pytest-api-tests](https://github.com/bryanzou78/pytest-api-tests) covers API-level contract testing, this project covers browser-based e2e testing in Python, along with API/UI cross-validation.

## Tech Stack

- Python 3.10
- pytest
- Playwright
- pytest-playwright
- requests

## Getting Started

```bash
# Clone the repo
git clone git@github.com:bryanzou78/playwright-tests.git
cd playwright-tests

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browser
playwright install chromium
```

## Running Tests

```bash
pytest tests/
```

## Tests

6 tests covering distinct Wikipedia user flows, plus one API/UI consistency check.

- `tests/test_wikipedia.py` — homepage load, search navigation to a specific article, in-article link navigation to a related topic, article section rendering, and a no-results search edge case
- `tests/test_wikipedia_api.py` — cross-checks Wikipedia's public REST API (`/api/rest_v1/page/summary/...`) against the rendered article page, verifying the title returned by the API matches what's actually displayed

## Fixtures

Shared setup lives in `conftest.py`:

- `page_on_wiki_homepage` / `page_on_einstein_article` — navigate to a starting page before a test runs
- `search` — factory fixture that returns a callable for performing a Wikipedia search with any term

## CI

Tests run automatically on every push and pull request via GitHub Actions.