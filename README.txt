# Flask Application with Snowflake Integration

This is a Flask web application that connects to a Snowflake database to retrieve and display application logs. The logs are categorized by log levels (`INFO`, `WARNING`, `ERROR`) and are displayed separately on the web interface.

## Features

- **Python 3.12.3**: The application is built using Python 3.12.3.
- **Flask 3.0.3**: Utilizes the Flask framework to handle web requests and render HTML templates.
- **Snowflake Integration**: Connects to a Snowflake database to retrieve logs from the `APPLICATION_LOGS` table.

## Prerequisites

Ensure you have the following installed on your system:

- **Docker**: To containerize and run the application.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://your-repository-url.git
cd my_app
run ./setup.sh in the folder my_app