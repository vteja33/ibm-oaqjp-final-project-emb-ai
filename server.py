"""
Flask server for Emotion Detection App.
Handles emotion detection and serves the homepage.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def emot_detector():
    """Handles emotion detection requests and returns emotion analysis."""
    text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    if result is None or result['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again!</b>"

    return (f"For the given statement, the system response is 'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
            f"and 'sadness': {result['sadness']}. The dominant emotion is "
            f"<b>{result['dominant_emotion']}</b>")

@app.route("/")
def render_index_page():
    """Renders the index HTML page."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
    