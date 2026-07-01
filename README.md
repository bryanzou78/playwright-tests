# playwright-tests

![CI](https://github.com/bryanzou78/playwright-tests/actions/workflows/tests.yml/badge.svg)

Browser automation tests for [Wikipedia](https://www.wikipedia.org) using Python and Playwright.

Built as a standalone testing project targeting a live third-party site, demonstrating the ability to write browser tests against an unfamiliar product. Where [pytest-api-tests](https://github.com/bryanzou78/pytest-api-tests) covers API-level contract testing, this project covers browser-based e2e testing in Python.

## Tech Stack

- Python 3.10
- pytest
- Playwright
- pytest-playwright

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

4 tests covering distinct Wikipedia user flows.

- `tests/test_wikipedia.py` — homepage load, search navigation to a specific article, in-article link navigation to a related topic, and article section rendering

## CI

Tests run automatically on every push and pull request via GitHub Actions.