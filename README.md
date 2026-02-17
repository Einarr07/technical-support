# Technical Support API

A Django REST Framework project designed for managing technical support tickets, customers, and technicians. This API
demonstrates the use of different view strategies (Function-Based vs. Class-Based), JWT authentication, and automated
auditing.

## 📋 Prerequisites

* Python 3.x
* Virtual Environment (venv)
* Docker (Optional)

## 🚀 First Steps & Installation

Follow these steps to set up the project locally.

### 1. Create and Activate Virtual Environment

Create an isolated environment for dependencies:

```bash
# Create venv
python -m venv venv

# Activate venv (Linux/macOS)
source venv/bin/activate

# Activate venv (Windows)
# .\venv\Scripts\activate
```

### 2. Install Dependencies

You can install the required packages individually or via the requirements file.2. Install Dependencies

````
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install django-crum
pip install drf-spectacular
````

or pip install -r requirements.txt

### 3. Database Migrations

Initialize the database schema for the apps.

```
# Create migrations for a specific app
python manage.py makemigrations <app_name>

# Apply migrations
python manage.py migrate

```

## 🏗️ Project Architecture & Apps

The system is modularized into several Django apps, each serving a specific purpose:

1. core
   Purpose: Manages base entities (Customers and Technicians).

Implementation: Uses Function-Based Views (FBV) to demonstrate manual API logic implementation.

2. support
   Purpose: Manages the main logic for Support Tickets.

Implementation: Uses Class-Based Views (CBV) and Generic Views.

Reference: Utilizes classes from Classy Django REST Framework for cleaner code.
[Class Django REST Framework](https://www.cdrf.co/)

3. accounts
   Purpose: Manages Users and Authentication.

Library: Uses djangorestframework-simplejwt for secure token-based authentication (JWT).

4. common
   Purpose: Utilities and shared logic.

Feature: Implements auditing (tracking who created/modified records) using django-crum.

5. docs
   Purpose: Configuration for API schema and documentation.

## 🛠️ Key Technologies & Features

Serialization: Serializers are defined within each app to handle data validation and JSON representation.

Auditing: django-crum captures the current user in the request, ensuring proper auditing of model creation and updates.

Authentication: JWT (JSON Web Token) via SimpleJWT.

Documentation: Automated API documentation using drf-spectacular.

## 📚 API Documentation

The project includes auto-generated documentation. Once the server is running (python manage.py runserver), you can
access:

Schema: /api/schema/

Swagger UI: /api/schema/swagger-ui/ (Interactive interface)

ReDoc: /api/schema/redoc/ (Clean, organized documentation)

Documentation reference: drf-spectacular
installation [Documentation](https://drf-spectacular.readthedocs.io/en/latest/readme.html#installation)