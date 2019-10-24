from flask import Flask, request, jsonify, render_template, flash, redirect, url_for
from textblob import TextBlob as tb
import speech_recognition as sr
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/predict',methods=['POST'])

def predict():
    a= request.form.get('movietext')
    if(not a):
        try:
            r = sr.Recognizer()
            f = request.files['file']  
            f.save(f.filename)
            sampleaudio = sr.AudioFile(f.filename)
            with sampleaudio as source:
                audio = r.record(source)
            a=r.recognize_google(audio)
            os.remove(f.filename)
        except KeyError:   
            return render_template('app.html', prediction_text='ERROR: Enter some text or audio') 
    blob=tb(a)
    rate=5+blob.sentiment.polarity*5
    rate=round(rate,1)
    output=rate
    return render_template('app.html', prediction_text='Rating: {}/10'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    a= data.get('movietext')
    blob=tb(a)
    rate=5+blob.sentiment.polarity*5
    rate=round(rate,1)
    output=rate
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)