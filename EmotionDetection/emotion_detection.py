import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    objc = { "raw_document": { "text": text_to_analyze } }

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = objc, headers = header)
    # Format the response as json
    format_response = json.loads(response.text)

    # Check responses status code
    if response.status_code != 200:
        # Status code thats not 200 and returns dictionary with None values
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None 
        }
    elif response.status_code == 200:
        # Status code of 200 returns dictionary with emotion values
        # Extract emotions from formatted response
        emotions = format_response['emotionPredictions'][0]['emotion']
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        
        # Store emotion scores
        emotion_scores = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score}
        # Determine the dominant emotion
        dominant_emotion = max(emotion_scores, key = emotion_scores.get)

        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion 
        }