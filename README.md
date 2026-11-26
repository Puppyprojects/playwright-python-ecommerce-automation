# Playwright Python E-commerce Automation Framework

An end-to-end web automation testing framework built using **Python, Playwright, Pytest, and Page Object Model (POM)**. This project automates important e-commerce workflows on the SauceDemo application, including login validation, product inventory management, sorting, cart operations, and checkout.

## Project Overview

This project demonstrates how to build a structured and reusable automation testing framework using Playwright with Python.

The framework follows the Page Object Model (POM) design pattern to separate test logic from page locators and reusable actions. Pytest is used for test execution, fixtures, test organization, and reporting.

**Application Under Test:** https://www.saucedemo.com/

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Playwright | Browser automation |
| Pytest | Test framework |
| Pytest-HTML | HTML test reporting |
| POM | Test framework design pattern |
| Git & GitHub | Version control |
| GitHub Actions | Workflow automation |

## Project Features

### 1. Login Testing
- Verify successful login with valid credentials.
- Verify login page title.
- Validate incorrect username and password.
- Verify locked-out user behavior.
- Validate empty username and password fields.

### 2. Inventory Testing
- Verify all six products are displayed.
- Add products to the shopping cart.
- Remove products from the shopping cart.
- Verify product sorting by price (low to high).
- Verify product sorting by name (Z to A).

### 3. End-to-End Checkout Testing
- Add a product to the cart.
- Verify the selected product in the cart.
- Enter customer information.
- Navigate through checkout overview.
- Complete the checkout process.
- Verify successful order confirmation.

### 4. Framework Features
- Page Object Model (POM) architecture.
- Reusable page classes and methods.
- Pytest fixtures for browser and page setup.
- Centralized configuration.
- HTML test reports.
- GitHub version control.

## Project Structure

```text
playwright-python-ecommerce-automation/
│
├── .github/
│   └── workflows/
│       └── playwright.yml
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   └── inventory_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_checkout_e2e.py
│
├── utils/
│   ├── __init__.py
│   └── config.py
│
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation and Setup

### Prerequisites

- Python 3.10 or above
- VS Code
- Git
- Basic knowledge of Python

### Step 1: Clone the Repository

```bash
git clone https://github.com/Puppyprojects/playwright-python-ecommerce-automation.git
```

### Step 2: Navigate to the Project

```bash
cd playwright-python-ecommerce-automation
```

### Step 3: Create a Virtual Environment

```bash
python3 -m venv venv
```

### Step 4: Activate Virtual Environment

**macOS / Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Install Playwright Browsers

```bash
playwright install
```

## Test Execution

### Run All Test Cases

```bash
python -m pytest tests/ -v -s
```

### Run Login Tests

```bash
python -m pytest tests/test_login.py -v -s
```

### Run Inventory Tests

```bash
python -m pytest tests/test_inventory.py -v -s
```

### Run End-to-End Checkout Test

```bash
python -m pytest tests/test_checkout_e2e.py -v -s
```

### Run Regression Tests

```bash
python -m pytest tests/ -m regression -v -s
```

## HTML Test Reporting

Generate an HTML report using:

```bash
python -m pytest tests/ -v -s --html=reports/report.html --self-contained-html
```

Open the generated report:

```bash
open reports/report.html
```

The HTML report provides:
- Passed test cases
- Failed test cases
- Execution duration
- Test execution summary

## Test Execution Results

The framework has been executed successfully, with the initial test suite showing:

- **Total test cases:** 11
- **Passed:** 11
- **Failed:** 0
- **Skipped:** 0

*Results reflect the recorded execution at the time of project development.*

## Key Learning Outcomes

Through this project, I gained practical experience in:

- Browser automation using Playwright with Python.
- Writing and executing automated test cases using Pytest.
- Implementing Page Object Model (POM).
- Creating reusable functions and fixtures.
- Handling locators, assertions, and web elements.
- Automating end-to-end e-commerce workflows.
- Generating and analyzing HTML test reports.
- Managing projects using Git and GitHub.

## Future Enhancements

- Add cross-browser testing for Chromium, Firefox, and WebKit.
- Integrate automated test execution with GitHub Actions.
- Add API testing using Playwright APIRequestContext.
- Implement screenshot capture on test failures.
- Improve test data management.
- Add detailed test execution reports.

## Repository

GitHub: https://github.com/Puppyprojects/playwright-python-ecommerce-automation

## Author

**Shreya Raj**

QA Automation | Python | Playwright | Pytest | Software Testing

