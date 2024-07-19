### README.md

```markdown
# Salary Aggregation and Telegram Bot

This project provides an application that aggregates salary data from a MongoDB database over different time intervals (hour, day, month) and serves the aggregated data through a FastAPI application. Additionally, it includes a Telegram bot that allows users to request aggregated salary data by sending JSON requests via Telegram messages.

## Project Structure

```
salary_aggregation/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── aggregator.py
├── telegram_bot/
│   ├── __init__.py
│   └── bot.py
├── data/
│   ├── sample_collection.bson
│   └── sample_collection.metadata.json
├── tests/
│   ├── test_aggregator.py
│   ├── test_main.py
│   └── test_bot.py
├── load_data.py
├── requirements.txt
├── README.md
└── pytest.ini
```

## Requirements

- Python 3.8+
- MongoDB
- Telegram Bot Token

## Installation

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd salary_aggregation
    ```

2. **Set up a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Start MongoDB service:**

    ```bash
    brew services start mongodb-community
    ```

5. **Load sample data into MongoDB:**

    ```bash
    python load_data.py
    ```

## Configuration

1. **Create a `.env` file in the root directory and add your Telegram bot token:**

    ```
    TELEGRAM_TOKEN=your_actual_telegram_token
    ```

## Running the Application

1. **Start the FastAPI application:**

    ```bash
    python -m app.main
    ```

2. **Start the Telegram bot:**

    ```bash
    python -m telegram_bot.bot
    ```

## Usage

### FastAPI Endpoint

- **Endpoint:** `/aggregate`
- **Method:** `POST`
- **Request Body:**
  
    ```json
    {
        "dt_from": "2022-09-01T00:00:00",
        "dt_upto": "2022-12-31T23:59:00",
        "group_type": "month"
    }
    ```

- **Response:**

    ```json
    {
        "dataset": [5906586, 5515874, 5889803, 6092634],
        "labels": ["2022-09-01T00:00:00", "2022-10-01T00:00:00", "2022-11-01T00:00:00", "2022-12-01T00:00:00"]
    }
    ```

### Telegram Bot

- **Command:** `/start`
  - **Description:** Welcomes the user and provides instructions.

- **Message:** JSON request with `dt_from`, `dt_upto`, and `group_type`.
  - **Example:**

    ```json
    {
        "dt_from": "2022-09-01T00:00:00",
        "dt_upto": "2022-12-31T23:59:00",
        "group_type": "month"
    }
    ```

  - **Response:** Aggregated salary data for the specified period and group type.

## Running Tests

1. **Install Testing Dependencies:**

    ```bash
    pip install pytest pytest-cov pytest-asyncio
    ```

2. **Run Tests:**

    ```bash
    pytest --cov=app --cov=telegram_bot --cov-report=term-missing
    ```

3. **Generate HTML Coverage Report:**

    ```bash
    pytest --cov=app --cov=telegram_bot --cov-report=html
    ```

## Acknowledgments

This project uses the following libraries:

- [FastAPI](https://fastapi.tiangolo.com/)
- [MongoDB](https://www.mongodb.com/)
- [python-telegram-bot](https://python-telegram-bot.readthedocs.io/)
- [pandas](https://pandas.pydata.org/)
- [pydantic](https://pydantic-docs.helpmanual.io/)
- [requests](https://docs.python-requests.org/en/latest/)
- [pytest](https://pytest.org/)
- [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio)


```

### Instructions to Start the Project from Scratch

1. **Clone the repository and navigate to the project directory:**

    ```bash
    git clone <repository_url>
    cd salary_aggregation
    ```

2. **Set up a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Start MongoDB service:**

    ```bash
    brew services start mongodb-community
    ```

5. **Load sample data into MongoDB:**

    ```bash
    python load_data.py
    ```

6. **Create a `.env` file with your Telegram bot token:**

    ```plaintext
    TELEGRAM_TOKEN=your_actual_telegram_token
    ```

7. **Start the FastAPI application:**

    ```bash
    python -m app.main
    ```

8. **Start the Telegram bot:**

    ```bash
    python -m telegram_bot.bot
    ```

9. **Run tests to ensure everything is working:**

    ```bash
    pytest --cov=app --cov=telegram_bot --cov-report=term-missing
    ```
