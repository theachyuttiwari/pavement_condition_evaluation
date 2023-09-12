from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import optuna

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check and process the uploaded file here
        # ...
        return render_template('results.html', results=results)  # Pass results to the template
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
