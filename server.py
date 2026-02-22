"""
 Import all required modules
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection  import emotion_detector
app = Flask("Emotion Detection  Analyzer")

@app.route("/")
def render_index_page():
    """
    Render the main index page of the Emotion Detection application.

    Returns:
        str: Rendered HTML template for the home page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotio_detector():
    """APi method used 
    Returns:
        str: result or excpetion message with empty result.
    """
    # Retrieve the text to detect emotions from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    empty_result = { 'anger': None,'disgust': None,'fear': None,'joy': None,'sadness': None} 
    try:
        # Pass the text to the sentiment_analyzer function and store the response
        result = emotion_detector(text_to_analyze)
        if result['joy'] is None:
            return empty_result ,400
        predicted_emotion = max(result, key=result.get)
        result['dominant_emotion'] = predicted_emotion
        final_result = ( f"For the given statement, the system response is {result}. "
                        f"The dominant emotion is {predicted_emotion}")
        print (final_result)
        return final_result,200
    except (TypeError, ValueError) as error:
        app.logger.error("Input error: %s", error)
        return "Invalid input provided", 400

    except RuntimeError as error:
        app.logger.error("Emotion detection failure: %s", error)
        return "Emotion detection failed", 500        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
