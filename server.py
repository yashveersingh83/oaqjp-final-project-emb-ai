from flask import Flask, render_template, request
from EmotionDetection.emotion_detection  import emotion_detector
app = Flask("Emotion Detection  Analyzer")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotio_detector():
    # Retrieve the text to detect emotions from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    empty_result ={
                    'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None
                    }
    
    try:
        # Pass the text to the sentiment_analyzer function and store the response
        result = emotion_detector(text_to_analyze)
        
        print(result)
        if result['joy'] is None:
            return empty_result ,400
        predicted_emotion = max(result, key=result.get)
        result['dominant_emotion'] = predicted_emotion    
        final_result = f"For the given statement, the system response is {result} .  The dominant emotion is {predicted_emotion}"
        print (final_result)
        return final_result,200
    except Exception as e:
        print("Error occurred at server :", e)
        return "Error occurred"
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)