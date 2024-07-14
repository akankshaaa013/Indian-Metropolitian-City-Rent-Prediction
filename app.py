# from django.shorcuts import render
import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
regmodel = pickle.load(open('regmodel.pkl','rb'))

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/predict_api', methods = ['POST'])

def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())))
    
    # ['BHK', 'Size', Area Type', 'City', Furnishing Status', Tenant Preffered', Bathroom', Point of Contact', Total Floor']
    
    # Loading all the pickle files.
    scalar = pickle.load(open('scaler.pkl','rb'))
    regression = pickle.load(open('regmodel.pkl','rb'))
    poly_transformation = pickle.load(open('poly_regs.pkl','rb'))
    
    