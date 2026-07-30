# API Automation Framework

## Overview

This project is a Python-based API Automation Framework built using FastAPI and Pytest. It demonstrates a clean automation framework architecture using reusable API methods, fixtures, configuration files, logging, HTML reports, and parameterized tests.

The framework is designed to be scalable and easy to maintain, following automation testing best practices.

---

## Tech Stack

* Python
* FastAPI
* Pytest
* Requests
* SQLAlchemy
* SQLite
* Pytest HTML Reports

---

## Framework Features

* CRUD API Testing
* Reusable Base API Client
* Product API Layer
* Pytest Fixtures
* Parameterized Tests
* Configuration Management
* Logging
* HTML Test Reports
* Request and Response Tracking
* Clean Project Structure

---

## Project Structure

```text
api/
config/
database/
logs/
reports/
tests/

main.py
conftest.py
requirements.txt
README.md
```

---

## Running the Project

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the FastAPI server

```bash
uvicorn main:app --reload
```

### Run all tests

```bash
python -m pytest
```

### Generate HTML Report

```bash
python -m pytest --html=reports/report.html
```

---

## Future Improvements

* GitHub Actions (CI/CD)
* Jenkins Integration
* Docker Support
* Linux Deployment
* Playwright UI Automation
* AI-assisted Test Automation
