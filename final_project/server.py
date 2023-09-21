"""
server.py - Emotion Detection Flask Application

This module contains the Flask application for performing emotion detection
on user-provided text. It defines the routes and functions necessary to
analyze text for emotions and display the results.

Usage:
- Start the Flask application to run the emotion detection service.

Author: Oscar Rincon
"""
# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def sent_analyzer():
    """
    Analyzes the emotion of a given text and returns the results.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response is None:
        return "Invalid input or an error occurred! Try again."
    return f"For the given statement, the system response is \
    'anger': {response.get('anger', 0)}, 'disgust': \
    {response.get('disgust', 0)}, 'fear':\
     {response.get('fear', 0)}, 'joy': \
     {response.get('joy', 0)} and 'sadness':\
      {response.get('sadness', 0)}.\
       The dominant emotion is \
       {response.get('dominant_emotion', 'None')}."

@app.route("/")
def render_index_page():
    """
    Renders the main application page over the Flask channel.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
