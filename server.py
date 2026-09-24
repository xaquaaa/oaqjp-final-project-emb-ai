from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def home_page():
    return render_template("index.html")
@app.route("/emotionDetector")
def sent_emotion_detec():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    return f"For the given statement, the system response is 'anger':{response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is <strong>{response['dominant_emotion']} </strong>"




if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)