
**SLR Project**

This project is a small web application that uses Simple Linear Regression (SLR) to make predictions.
The app has a front-end page, a Flask backend, and one SLR model file.

**What is Simple Linear Regression?**

Simple Linear Regression (SLR) is a basic machine learning method used to predict one value based on another value.

It finds a straight line that best fits the data.

The line has the formula:

              y = m*x + c


Where:

x = input value

y = predicted output

m = slope

How the App Works

User enters a number on the webpage.

The webpage sends the number to Flask.

Flask calls the SLR function in slr_model.py.

The model calculates the prediction using 
          
                y = m*x + c.

The predicted value is shown on the screen.

c = intercept

Once the line is found, we can use it to predict new values.

**Requirements:**

Install needed packages:

pip install flask numpy

**How to Run:**

python app.py

**Developer Details:**

Name: Nidamanuri Pranavi Lakshmi Sai

phone no: 8142984404

Gmail : pranavinidamanuri444@gmail.com
