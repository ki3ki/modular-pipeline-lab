# MLOps Data Ingestion Pipeline

## Overview

This project demonstrates the foundational components of an MLOps-style data ingestion pipeline. The pipeline extracts data from a REST API, validates configurations, logs execution details, handles failures with retries, and stores processed data with metadata.

The project was built to understand production-oriented software engineering practices that are commonly used in data engineering and machine learning systems.

---

## Features

* Environment-based configuration management
* Configuration validation
* Structured logging
* REST API data extraction
* Retry mechanism with exponential backoff
* Error handling and monitoring
* Data storage with metadata
* Modular project architecture
* Atomic file writing for safer storage

---

## Project Structure

```text
project/
│
├── config.py          # Environment-specific settings
├── validator.py       # Configuration validation
├── logger.py          # Logging configuration
├── ingestion.py       # API data extraction
├── storage.py         # Data persistence
├── main.py            # Pipeline orchestration
│
├── data/              # Generated output files
├── logs/              # Pipeline logs
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Architecture

```text
Configuration
      ↓
Validation
      ↓
Data Extraction
      ↓
Retry & Error Handling
      ↓
Data Storage
      ↓
Logging
```

---

## Technologies Used

* Python 3.x
* Requests
* Python-dotenv
* Logging Module
* JSON

---

## Workflow

1. Load environment configuration
2. Validate configuration settings
3. Extract data from API
4. Handle transient failures using retries
5. Store extracted data with metadata
6. Log pipeline execution details

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
ENVIRONMENT=development
API_KEY=your_api_key
```

---

## Running the Pipeline

```bash
python main.py
```

Successful execution will:

* Create log entries in the `logs/` directory
* Save extracted data in the `data/` directory
* Store metadata such as extraction timestamp and record count

---

## Example Output Structure

```json
{
  "metadata": {
    "extraction_time": "2026-06-05T10:30:00",
    "record_count": 20
  },
  "data": [
    ...
  ]
}
```

---

## Learning Outcomes

This project helped reinforce important MLOps and software engineering concepts:

* Configuration management
* Pipeline modularity
* Logging and observability
* Fault tolerance
* Retry strategies
* Data validation
* Reproducible workflows

---

## Future Improvements

* Unit testing
* Database integration
* Docker containerization
* CI/CD pipeline integration
* Workflow orchestration using Airflow or Prefect
* Cloud storage integration

---
