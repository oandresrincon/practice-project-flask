import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Create the input JSON
    myobj = { "raw_document": { "text": text_to_analyze } }


    # Make a POST request to the Watson NLP API
    response = requests.post(url, json=myobj, headers=header)

    # Check the HTTP status code
    result = {}  # Initialize the result dictionary
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        result = formatted_response['emotionPredictions'][0]['emotion']
        max_key = max(result, key=lambda k: result[k])
        result['dominant_emotion'] = max_key
    elif response.status_code == 400:         
        result['anger'] = None
        result['disgust'] = None
        result['fear'] = None
        result['joy'] = None
        result['sadness'] = None
        result['dominant_emotion'] = None



    return {'result': result}

# Example usage:
# result = emotion_detector("This is a sample text for emotion analysis.")
# print(result)
