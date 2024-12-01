
This project uses the **Soft UI Dashboard Flask** template from [AppSeed](https://appseed.us/product/soft-ui-dashboard/flask/) as its website framework.


Here’s the updated `README.md` section with the Docker instructions listed first:

---

### How to Run the Application

You can set up and run the application using one of the following methods:

#### Option 1: Using Docker (Recommended)
1. Build the Docker image:
   ```bash
   make build-frontend
   ```
2. Run the Docker container:
   ```bash
   make run-frontend
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
6. Run the application:
   ```bash
   flask run
   ```
7. Visit the application in your browser at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

