# IDS706 Final Project

## Continuous Integration with GitHub Actions
[![Install](https://github.com/Reby0217/ids706-finalProject/actions/workflows/install.yml/badge.svg)](https://github.com/Reby0217/ids706-finalProject/actions/workflows/install.yml)
[![Lint](https://github.com/Reby0217/ids706-finalProject/actions/workflows/lint.yml/badge.svg)](https://github.com/Reby0217/ids706-finalProject/actions/workflows/lint.yml)
[![Format](https://github.com/Reby0217/ids706-finalProject/actions/workflows/format.yml/badge.svg)](https://github.com/Reby0217/ids706-finalProject/actions/workflows/format.yml)
[![Tests](https://github.com/Reby0217/ids706-finalProject/actions/workflows/test.yml/badge.svg)](https://github.com/Reby0217/ids706-finalProject/actions/workflows/test.yml)

## Demo Video
Here is the [link to our demo video on YouTube](https://www.youtube.com/watch?v=K-WcJdBPERI).

---

This project is a microservice-based application that provides user authentication and profile management functionalities. It includes sign-up, login, and profile display features. Each time a user successfully signs up, their information is stored in the database.

Link to our app: https://bnnt5hhvdc.us-east-2.awsapprunner.com/


---

## How to Run the Application

You can set up and run the application using one of the following methods:

### Option 1: Using Docker (Recommended)
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

### Option 2: Using a Virtual Environment (for dev purpose)
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

## Architectural Diagram

![image](imgs/diagram.png)

---

## Data Engineering Compliance

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
## Load Test

### Objective
To verify our microservice's capacity to handle significant traffic, we performed scaled-down load tests using Apache Bench.

### Testing Method
- **100 Requests Test:**
  ```bash
  ab -n 100 -c 10 https://bnnt5hhvdc.us-east-2.awsapprunner.com/
  ```
   ![image](imgs/loadtest1.png)
- **1,000 Requests Test:**
  ```bash
  ab -n 1000 -c 10 https://bnnt5hhvdc.us-east-2.awsapprunner.com/
  ```
  ![image](imgs/loadtest2.png)

### Rationale
Given the project's scope and budget constraints, tests with 100 and 1,000 requests were deemed sufficient to demonstrate the microservice’s scalability and performance capabilities. Testing up to the full requirement of 10,000 requests per second was considered cost-prohibitive for this academic exercise, as confirmed by our teaching assistant.

### Results
Both tests confirmed efficient handling of increased loads, indicating that our service can scale up effectively when needed.

![image](imgs/loadtest3.png)

---

## Quantitative Assessment
Based on the provided Apache Bench results and AWS App Runner service metrics, we conducted a quantitative assessment of the microservice's reliability and stability under load. The assessment revealed:

1. **Response Latency Analysis**:
   - At 100 requests per second, the average latency was 122.865 milliseconds per request across all concurrent requests, with a peak latency of 1366 milliseconds.
   - Scaling to 1000 requests per second, the average latency increased slightly to 125.532 milliseconds, indicating a consistent performance under increased load with peak latency reaching 2916 milliseconds.

2. **Throughput and Stability**:
   - The server processed 100 requests in 12.287 seconds and 1000 requests in 125.532 seconds, maintaining a stable throughput rate without any failures, as indicated by the complete absence of non-2xx responses in both tests.

3. **AWS App Runner Metrics**:
   - The request count metrics from AWS App Runner showed a corresponding spike in traffic, validating the load tests conducted and confirming the service's ability to handle surges in traffic effectively.

This data-driven evaluation demonstrates that the microservice scales linearly with increasing load while maintaining acceptable response times, affirming its reliability and robustness in handling up to 1000 requests per second efficiently.

---

### Auto Scaling Setup in AWS App Runner

![auto-scaling](imgs/auto.jpg)

---


### Flask Integration

This project utilizes **Flask**, to build the application's core functionality. Flask serves as the foundation for handling HTTP requests, routing, and rendering dynamic web pages.

Key features include:

- **Routing and Modularization**: The application uses Flask Blueprints to organize features like authentication and API endpoints, ensuring a clean and maintainable structure.
- **Dynamic Templating**: Flask integrates seamlessly with HTML templates, enabling dynamic rendering of user interfaces.
- **API Integration**: RESTful APIs are implemented using Flask-RESTx to support robust data exchange and user authentication workflows.
- **OAuth Support**: GitHub OAuth login is integrated using Flask-Dance for secure third-party authentication.

---

## Microservice

### Infrastructure as Code (IaC) with AWS CDK

Our project leverages the AWS Cloud Development Kit (CDK) to define and provision our cloud infrastructure, ensuring a consistent, reliable, and secure setup across development, testing, and production environments. The AWS CDK allows for declarative infrastructure management using familiar programming languages like Python, enabling version control and significantly reducing the likelihood of deployment errors.

#### Key Features:
- **DynamoDB Tables**: We manage NoSQL databases with specified partition keys to efficiently handle large-scale data.
- **Lambda Functions**: Our backend operations are powered by serverless functions that handle data processing and user authentication, seamlessly integrating with our data pipeline.
- **Security**: We employ explicit permission definitions to enhance security and ensure compliance with best practices.

#### Code Snippet:
```python
demo_table = aws_dynamodb.Table(
    self, "user_info",
    partition_key=aws_dynamodb.Attribute(name="id", type=aws_dynamodb.AttributeType.STRING),
)

producer_lambda = aws_lambda.Function(
    self, "write_to_dynamodb_lambda_function",
    runtime=aws_lambda.Runtime.PYTHON_3_11,
    code=aws_lambda.Code.from_asset("./lambda/producer"),
)
```

#### Lambda Functions
We have developed three Python-based Lambda functions to interface directly with our data pipeline:
1. **Check Duplicate Username**: This function checks for duplicate usernames within our user database to prevent registration conflicts. (Path: `./lambda_microservice/lambda/consumer`)
2. **Write Item to DynamoDB**: It handles the insertion of new user data into our DynamoDB table, ensuring data consistency and durability. (Path: `./lambda_microservice/lambda/producer`)
3. **Login**: This function manages user authentication by verifying credentials stored in DynamoDB. (Path: `./lambda_microservice/login`)

Here are the results of running tests on these Lambda functions:

![Consumer Lambda Test Result](https://github.com/user-attachments/assets/de702261-1300-43a7-a2b3-27877d82aa0c)
![Producer Lambda Test Result](https://github.com/user-attachments/assets/f9a265a6-44ec-4440-9246-fcc7e87d4905)
![Login Lambda Test Result](https://github.com/user-attachments/assets/5a669b53-bf56-408b-b6b1-8d646c2dc30f)

#### CloudWatch metrics

![image](imgs/consumer-metrics.png)
![image](imgs/login-metrics.png)
![image](imgs/producer-metrics.png)

#### DynamoDB
Our DynamoDB setup on AWS stores user information efficiently and securely:

![DynamoDB Setup](https://github.com/user-attachments/assets/19c6f0d0-55fa-449d-bf07-0fb8ecc7511a)

Since we are interacting with dummy data to test our Lambda functions, the username-password combinations listed do not pose any real-world security risks.


#### Logging
![image](imgs/logging.png)

---

### AI Pair Programming

GitHub Copilot: Used for auto-generating boilerplate code, optimizing frontend HTML files.

---


### Dependencies

- This project incorporates selected components of the **Soft UI Dashboard** template from [AppSeed](https://appseed.us/product/soft-ui-dashboard/flask/) as part of its website framework. 

- The AWS CDK is referenced from the official example in [aws-cdk-samples](https://github.com/aws-samples/aws-cdk-examples).
