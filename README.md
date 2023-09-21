# Emotion Detection Flask Application

This Flask application allows you to perform emotion detection on user-provided text. It defines the routes and functions necessary to analyze text for emotions and display the results.

## Usage

1. Start the Flask application to run the emotion detection service.

## Author

- **Author:** Oscar Rincon

## Getting Started

### Prerequisites

Make sure you have the required libraries installed:

```bash
pip install flask
```

## Running the Application
To run the application, execute the following command:

bash
Copy code
python server.py
By default, the application will be available at http://localhost:5000.

Routes
Emotion Detection
Endpoint: /emotionDetector (GET)

This route analyzes the emotion of a given text and returns the results.

Parameters:

textToAnalyze: The text to analyze for emotions.
Example usage:

http
Copy code
GET /emotionDetector?textToAnalyze=I am so happy!
Response:
For the given statement, the system response is:
- 'anger': 0,
- 'disgust': 0,
- 'fear': 0,
- 'joy': 0.8,
- 'sadness': 0.2.
The dominant emotion is 'joy'.
Home Page
Endpoint: / (GET)

This route renders the main application page over the Flask channel.

