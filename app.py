import numpy as np
from flask import Flask, request, jsonify, render_template
from model import summarizer
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_text = request.form['input']
    summarized = summarizer(input_text)

    return render_template('index.html', summary=summarized)


if __name__ == "__main__":
    app.run(debug=True)