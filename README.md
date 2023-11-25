# Katana ML Skipper Web API

Web API implements external access endpoints.

## Table of Contents

- [Introduction](#introduction)
  - [Supported platform](#supported-platform)
  - [TODO](#todo)
- [Features](#features)
- [Instructions](#instructions)
  - [Getting started](#getting-started)
  - [Run the service without Docker](#run-the-service-without-docker)
  - [Run the service with Docker](#run-the-service-with-docker)
- [Structure](#structure)
- [Contribution](#contribution)


## Introduction

Social Media Analyzer is a powerful tool designed to extract data from various social media platforms. It offers a streamlined and efficient way to crawl and collect information from platforms such as Playstore, Youtube, Appstore, Website, Reddit, Google News.

### Supported platform

- Playstore
- Appstore
- Youtube
- Website
- Reddit (Often return an empty list)
- Google News (Not very useful)

### TODO


## Features

- **Data Crawling:** The tool enables you to crawl and extract data from social media platforms effortlessly.
- **Data Storage:** Extracted data can be saved in [PostgreSQL](https://www.postgresql.org/).


## Instructions

### **Getting started**

1. Install [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. Install [PostgreSQL](https://www.postgresql.org/).
3. Open terminal and clone the project.

### **Run the service without Docker**

1. Move to the project's location:

```bash
cd path/to/Social-Media-Analyzer
```

```bash
cd app
```

2. Create virtual environment (Ensure that you have installed [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) in your device):

```bash
conda create -n sma python=3.10
```

```bash
conda activate sma
```

3. Install libraries:

```bash
pip install -r requirements.txt
```

4. Create database (Optional if using only Scrapper module):

```bash
python setup.py
```

5. Start FastAPI:

```bash
python endpoint.py
```


### **Run the service with Docker**

1. Move to the project's location:

```bash
cd path/to/Social-Media-Analyzer
```

2. Run command:

```bash
docker-compose up --build
```

**Check the Swagger:** `http://127.0.0.1:4000/api/v1/social-medial-tool/tasks/docs#`

## Structure

```
.
│   docker-compose.yml
│   Dockerfile
│   README.md
│
└───app
    │   requirements.txt      # required library
    │   config.py             # Global variables
    │   endpoint.py           # Final endpoint
    │
    ├───alembic               # Data migration
    │
    ├───analyzer              # Analyzer module (Currently unused)
    │
    ├───database              # Database settings
    │
    ├───notifier              # Notifier module
    │
    ├───routers               # Endpoints for scrapper, analyzer, notifier modules
    │
    └───scrapper              # Scrapper module
        │
        └───core              # Core functions for crawling data 
```

## Contribution

Contributions to the Social Media Analyzer are welcome! If you encounter any issues, have ideas for improvements, or would like to add new features, feel free to submit a pull request or create an issue in the repository.

---
