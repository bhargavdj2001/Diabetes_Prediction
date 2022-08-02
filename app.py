from flask import Flask,request, url_for, redirect, render_template  ## importing necessary libraries
import pickle  ## pickle for loading model(Diabetes.pkl)
import pandas as pd  ## to convert the input data into a data frame for giving as a input to the model

app = Flask(__name__)  

model = pickle.load(open("Diabetes.pkl", "rb"))  ##loading model


@app.route('/', methods=['POST', 'GET'])             ## Defining main index route
def home():
    if request.method=='POST':
        text1 = request.form['1']      
        text2 = request.form['2'] 
        text3 = request.form['3']
        text4 = request.form['4']
        text5 = request.form['5']
        text6 = request.form['6']
        text7 = request.form['7']
        text8 = request.form['8']

        row_df = pd.DataFrame([pd.Series([text1,text2,text3,text4,text5,text6,text7,text8])])  ### Creating a dataframe using all the values
        prediction=model.predict_proba(row_df) ## Predicting the output
        output='{0:.{1}f}'.format(prediction[0][1], 2)    ## Formatting output
        return render_template('index.html', t=1, out = float(output))
    else:
        return render_template('index.html', t=0)


if __name__ == '__main__':
    app.run(debug=True) 