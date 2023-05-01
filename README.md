# Independent Study on Financial Education and Retail Trading Activity

This repository contains the code used to conduct an independent study on the relationship between financial education and retail trading activity. The analysis is carried out using Python and sklearn, within a virtual environment to manage dependencies.

## Getting Started

These instructions will guide you on how to set up the project and run the code on your local machine.

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setting up the Virtual Environment

To isolate the project's dependencies, we use a Python virtual environment. Follow these steps to create and activate the environment:

1. Navigate to the project's root directory in your terminal.
2. Run the following command to create a new virtual environment named `sklearn-venv`:

    ```
    python -m venv sklearn-venv
    ```

3. Activate the virtual environment. On Windows, run:

    ```
    .\sklearn-venv\Scripts\activate
    ```

    On Unix or MacOS, run:

    ```
    source sklearn-venv/bin/activate
    ```

### Installing the Dependencies

With the virtual environment activated, you can install the project's dependencies using the `requirements.txt` file:
    ```
    pip install -r requirements.txt
    ```

This will install all required Python packages including sklearn and its dependencies.

### Running the Code

Once the environment is set up and dependencies are installed, you can run the main Python script:
    ```
    python main.py
    ```


## Study Overview

This project investigates the impact of financial education on retail trading activity. It uses machine learning models to predict trading behaviors based on various factors, including individuals' level of financial education. The goal is to understand whether and how education influences trading habits, which can inform efforts to improve financial literacy and promote responsible investing.
