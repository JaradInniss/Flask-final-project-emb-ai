from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index():
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    response = (f"For the given statement '{text_to_analyze}' the system response is:"
                    f"Anger: {result['anger']}"
                    f"Disgust: {result['disgust']}"
                    f"Fear: {result['fear']}"
                    f"Joy: {result['joy']}"
                    f"Sadness: {result['sadness']}"
                    "----------------------------"
                    f"The Dominant Emotion is {result['dominant_emotion']}")
    
    return response

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)