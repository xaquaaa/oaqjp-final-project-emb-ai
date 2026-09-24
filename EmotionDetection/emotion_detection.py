import requests
import json

#FUNCTION emotion_detector to run emotion detection
def emotion_detector(text_to_analyze):
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    #custom header for emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    #request paylod in desired format
    myobj = { "raw_document": { "text": text_to_analyze } }

    #sending a post request for emotion detection service
    response = requests.post(url, json=myobj, headers=header)

    #error handling when input is empty and server responds 400
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    #format the response to dict using json
    formatted_response = json.loads(response.text)

    #extracting required emotions
    anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]

    emotions = {
        "anger":anger_score,
        "disgust":disgust_score,
        "fear":fear_score,
        "joy":joy_score,
        "sadness":sadness_score
    }

    #find dominant emotion
    dominant_emotion = max(emotions, key = emotions.get)

    #formatted output response
    formatted_emotions = {
        "anger":anger_score,
        "disgust":disgust_score,
        "fear":fear_score,
        "joy":joy_score,
        "sadness":sadness_score,
        "dominant_emotion": dominant_emotion       
    }

    return formatted_emotions
