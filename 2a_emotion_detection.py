import requests
import json


def emotion_detector(text_to_analyse):
    if text_to_analyse is None:
        return {'message':'Please enter some text as input'}
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputjson = { "raw_document": { "text": text_to_analyse } }
    try:
      response = requests.post(url,json=inputjson,headers=headers)
      formatted_output = json.loads(response.text)
      print(formatted_output)
    except:
        print('Error occured')
