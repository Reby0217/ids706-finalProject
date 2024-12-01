# IDS706 Final Project

## Continuous Integration with GitHub Actions
[![Install](https://github.com/Reby0217/ids706-finalProject/actions/workflows/install.yml/badge.svg)](https://github.com/Reby0217/ids706-finalProject/actions/workflows/install.yml)
[![Lint](https://github.com/Reby0217/ids706-finalProject/actions/workflows/lint.yml/badge.svg)](https://github.com/Reby0217/ids706-finalProject/actions/workflows/lint.yml)
[![Format](https://github.com/Reby0217/ids706-finalProject/actions/workflows/format.yml/badge.svg)](https://github.com/Reby0217/ids706-finalProject/actions/workflows/format.yml)
[![Tests](https://github.com/Reby0217/ids706-finalProject/actions/workflows/test.yml/badge.svg)](https://github.com/Reby0217/ids706-finalProject/actions/workflows/test.yml)

---

This project incorporates selected components of the **Soft UI Dashboard Flask** template from [AppSeed](https://appseed.us/product/soft-ui-dashboard/flask/) as part of its website framework.


---

### How to Run the Application

You can set up and run the application using one of the following methods:

#### Option 1: Using Docker (Recommended)
1. Build the Docker image:
   ```bash
   make docker-build-front
   ```
2. Run the Docker container:
   ```bash
   make docker-run-front
   ```
3. Visit the application in your browser at: [http://localhost:5085/](http://localhost:5085/) 

---

#### Option 2: Using a Virtual Environment
1. Install `virtualenv`:
   ```bash
   pip3 install virtualenv
   ```
2. Create a virtual environment:
   ```bash
   virtualenv env
   ```
3. Activate the virtual environment:
   ```bash
   source env/bin/activate
   ```
4. Install the required dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
5. Set environment variables:
   ```bash
   export FLASK_APP=run.py
   export FLASK_ENV=development
   ```
6. Navigate to the `frontend` directory and run the application:
   ```bash
   cd frontend
   flask run
   ```
7. Visit the application in your browser at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---
### Data Engineering Compliance

This project leverages **SQLAlchemy**, a specialized library for managing relational databases, to handle and process data efficiently. All project data is stored in a SQLite database located at `frontend/apps/db.sqlite3`.

1. **Database Management**:
   - SQLAlchemy is used to define and manage database models, such as `Users` and `OAuth`, facilitating CRUD operations and relationships using `ForeignKey` and `relationship`.

2. **Data Storage**:
   - The SQLite database (`frontend/apps/db.sqlite3`) serves as the primary storage for user data, authentication tokens, and OAuth details, ensuring a lightweight and portable data solution.

3. **Authentication and Token Management**:
   - Secure password storage is implemented using **hashlib** for hashing and salting passwords.
   - Token-based authentication uses **PyJWT** to generate and validate JSON Web Tokens for secure API access.

4. **Data Validation and Querying**:
   - SQLAlchemy's query interface supports dynamic data retrieval and filtering, such as user authentication and JWT generation.
   - Form inputs for login and registration are validated to ensure consistent, clean data in the database.
