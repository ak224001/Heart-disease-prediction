# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:55:44 2020

@author: Aditya
"""


import numpy as np
from flask import Flask, redirect, url_for, request ,render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb'))

@app.route('/')
def home():
    return render_template('HDP_Form.html')


@app.route('/predict',methods = ['POST', 'GET'])
def predict():
   if request.method == 'POST':
      #features = [print(x) for x in request.form]
      features = request.form.to_dict()
      #print(features)
      heart_data=[]
      for key,value in features.items():
          heart_data.append(value)
      ff=[]
      #final_features = [try: int(x) for x in heart_data]
      for x in heart_data:
          try:
              ff.append(int(x))
          except:
              ff.append(float(x))
      print(ff)
      ff2 = [np.array(ff)]
      scaled_ff = scaler.transform(ff2)
      prediction = model.predict(scaled_ff)
      print(prediction)
      if int(prediction)==0:
          prediction = "No Heart Disease Found"
      else:
          prediction = "Yes Heart Disease Found"
      return render_template("out.html",result = prediction)
  

if __name__ == '__main__':
   #app.run(debug = True)
   app.run(host='0.0.0.0',port='8080')