from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# ---- Simple Linear Regression Model ----
# y = m*x + c
m = 2.5   # slope (example)
c = 5     # intercept (example)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_val = float(request.form['feature'])
        prediction = m * input_val + c
        return render_template('index.html',
                               prediction_text=f"Predicted Value: {prediction:.2f}",
                               input_val=input_val)
    except:
        return render_template('index.html', prediction_text="Please enter a valid number.")

if __name__ == "__main__":
    app.run(debug=True)
