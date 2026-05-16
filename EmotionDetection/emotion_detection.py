import requests
import json


def emotion_detector(text_to_analyze):

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    # Create the payload with the text to be analyzed
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Set the headers with the required model ID for the API
    header = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    # Make a POST request to the API
    response = requests.post(url, json=myobj, headers=header)

    # Convert response text into a dictionary
    formatted_response = json.loads(response.text)

    # Extract emotion scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Store emotions in a dictionary
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    # Find dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return the required output format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }