from flask import Flask, request, jsonify, render_template
from textblob import TextBlob as tb

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    a= request.form.get('movietext')
    blob=tb(a)
    rate=5.333333333333333+blob.sentiment.polarity*4.5
    rate=round(rate,1)
    output=rate
    return render_template('index.html', prediction_text='Rating: {}/10'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    a= data.get('movietext')
    blob=tb(a)
    rate=5.333333333333333+blob.sentiment.polarity*4.5
    rate=round(rate,1)
    output=rate
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)