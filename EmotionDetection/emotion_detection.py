import requests, json

def emotion_detector(text_to_analyse: str):
    '''Function to run emotion detection'''

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_data = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url = url, json = input_data, headers = headers)
    if response.status_code == 200:
        formatted_output = json.loads(response.text)
        extracted_output = formatted_output['emotionPredictions'][0]['emotion']
        extracted_output['dominant_emotion'] = max(extracted_output, key=extracted_output.get)
        return extracted_output
    elif response.status_code == 400:
        return { "anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}

