# BTC Predictor Web App Frontend

## Instructions
1. Create Python environment using pip or pipenv:

    ```
    pip install -r requirments.txt
    ```

    or

    ```
    pipenv install
    ```

2. Run the app:

    ```
    python run_dash.py
    ```
    or
    ```
    $Env:FLASK_APP="frontend/btc_dash:app"
    flask run
    ```
3. Open the app on your browser:

    ```
    localhost:5000
    ```

## Tech Stack
Python

Plotly Dash

Flask

## Local Testing
To run local testing, formatting, and linting, please do:

```
tox
```

## CI/CD
Testing, formatting, and linting pipeline is run on Github Action using `.github/workflows/frontend.yml`.

