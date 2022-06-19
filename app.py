import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model= pickle.load(open('police.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=["POST"])
def predict():

   
    #sex
    sex = request.form['Sex']
    if sex == "male":
        sex = 1
    elif sex == "female":
        sex = 0
        
    age = request.form['Age']
    age = int(age)
   
    height = request.form['Height']
    height = float(height) 
    
    credentials = request.form['Fitness']
    if credentials == "Yes":
        credentials = 1
    elif credentials == "No":
        credentials = 0
     
    
    fitness = request.form['Fitness']
    if fitness == "Yes":
        fitness = 1
    elif fitness == "No":
        fitness = 0
    
    exercise = request.form['exercise score']
    exercise = int(exercise)
   
    int_features = [sex,age,height,credentials,fitness,exercise]
    final_features = [int_features]
    prediction = model.predict(final_features).round(2)
    
    if prediction[0]==0:
        product='This Applicant is not suitable to be Recruited into the Nigerian Police Force'
    else:
        product='This Applicant Satisfied all the Requirements to join the  Nigerian Police Force'

	
    return render_template('result.html', sex=sex,age=age,
     height=height,fitness=fitness,exercise=exercise,credentials=credentials,
                           prediction_text=product)



if __name__ == "__main__":
    app.run(debug=True)
    
    
