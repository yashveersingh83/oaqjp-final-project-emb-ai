import requests
def emotion_detector(text_to_analyse):
    #if not text_to_analyse:
    #    return None

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputjson = {"raw_document": {"text": text_to_analyse}}

    try:
        response = requests.post(url, json=inputjson, headers=headers)
        print (f' res   : {response}')
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None
            }

        formatted_output = response.json()

        return formatted_output['emotionPredictions'][0]['emotion']

    except Exception as e:
        print("API Error:", e)
        return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None
            }