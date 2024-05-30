# Polls App

The polls app is a Django application designed to create and manage polls. Users can vote on various questions, and administrators can create, edit, and delete polls through the admin interface.

## Documentation

Detailed documentation for Django 4.2 is available [here](https://docs.djangoproject.com/en/4.2/).

## Setup

To set up the environment and install Django, follow these steps:

1. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

2. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

3. Install Django:

    ```bash
    (venv)$ python -m pip install Django
    ```

## Python Version Compatibility

To check which Python versions are compatible with Django 4.2, refer to the official documentation [here](https://docs.djangoproject.com/en/4.2/faq/install/#faq-python-version-support).

## Usage

After setting up the environment and installing Django, you can run the polls app locally. Use the following commands to start the development server:

```bash
(venv)$ python manage.py runserver 0:8000
```
