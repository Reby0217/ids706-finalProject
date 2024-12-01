# IDS706 Final Project

## Continuous Integration with GitHub Actions
[![Install](https://github.com/Reby0217/ids706-finalProject/actions/workflows/install.yml/badge.svg)](https://github.com/Reby0217/ids706-finalProject/actions/workflows/install.yml)
[![Lint](https://github.com/Reby0217/ids706-finalProject/actions/workflows/lint.yml/badge.svg)](https://github.com/Reby0217/ids706-finalProject/actions/workflows/lint.yml)
[![Format](https://github.com/Reby0217/ids706-finalProject/actions/workflows/format.yml/badge.svg)](https://github.com/Reby0217/ids706-finalProject/actions/workflows/format.yml)
[![Tests](https://github.com/Reby0217/ids706-finalProject/actions/workflows/test.yml/badge.svg)](https://github.com/Reby0217/ids706-finalProject/actions/workflows/test.yml)

---

This project incorporates selected components of the **Soft UI Dashboard** template from [AppSeed](https://appseed.us/product/soft-ui-dashboard/flask/) as part of its website framework.


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

This project utilizes **SQLAlchemy**, a Python SQL toolkit that allows developers to access and manage SQL databases using Pythonic domain language. All data is stored in a lightweight SQLite database located at `frontend/apps/db.sqlite3`.

1. **Database Management**:
   - The project defines and manages database models like `Users` and `OAuth` using SQLAlchemy, enabling efficient CRUD operations and managing relationships with `ForeignKey` and `relationship`.

   - **Users Table Overview**:
      - **id**: Unique identifier for each user (primary key).  
      - **username**: Unique username for the user.  
      - **email**: Unique email address.  
      - **password**: Securely hashed password.  
      - **oauth_github**: Optional GitHub OAuth identifier.  
      - **api_token**: Authentication token for API access.  
      - **api_token_ts**: Timestamp of token creation.

2. **Data Storage**:
   - User data, authentication tokens, and OAuth details are stored in the SQLite database, providing a portable and reliable storage solution.

3. **Authentication and Security**:
   - **hashlib** ensures secure password storage with hashing and salting techniques.  
   - **PyJWT** enables token-based authentication, generating and validating secure JSON Web Tokens.

4. **Data Validation and Querying**:
   - SQLAlchemy's query interface supports dynamic data retrieval and filtering, critical for user authentication and API workflows.  
   - Form inputs for login and registration are validated to ensure clean and consistent database records.  

---

### Flask Integration

This project utilizes **Flask**, to build the application's core functionality. Flask serves as the foundation for handling HTTP requests, routing, and rendering dynamic web pages.

Key features include:

- **Routing and Modularization**: The application uses Flask Blueprints to organize features like authentication and API endpoints, ensuring a clean and maintainable structure.
- **Dynamic Templating**: Flask integrates seamlessly with HTML templates, enabling dynamic rendering of user interfaces.
- **API Integration**: RESTful APIs are implemented using Flask-RESTx to support robust data exchange and user authentication workflows.
- **OAuth Support**: GitHub OAuth login is integrated using Flask-Dance for secure third-party authentication.

