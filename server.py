"""
Flask application for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index():
    """
    Render the home page.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the emotion of the provided text and return response.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Invalid text! Please Try Again!"

    result = emotion_detector(text_to_analyze)

    # Ensure result is valid and dominant_emotion exists
    if not result or result.get("dominant_emotion") is None:
        return "Invalid text! Please Try Again!"

    response = (
        f"For the given statement '{text_to_analyze}' the system response is: "
        f"'Anger': {result.get('anger')}, "
        f"'Disgust': {result.get('disgust')}, "
        f"'Fear': {result.get('fear')}, "
        f"'Joy': {result.get('joy')}, "
        f"'Sadness': {result.get('sadness')}. "
        f"The Dominant Emotion is {result.get('dominant_emotion')}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
    