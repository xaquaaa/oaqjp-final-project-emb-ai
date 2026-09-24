"""FLASK SERVER FOR EMOTION DETECTION."""

from flask import Flask, request, render_template

from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detection")


@app.route("/")
def home_page():
    """RENDER THE HOME PAGE."""
    return render_template("index.html")


@app.route("/emotionDetector")
def sent_emotion_detec():
    """DETECT EMOTION FROM USER TEXT."""

    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return(
        f"For the given statement, the system response is"
        f"'anger':{response['anger']},"
        f"'disgust': {response['disgust']},"
        f"'fear': {response['fear']},"
        f"'joy': {response['joy']} and"
        f"'sadness': {response['sadness']}."
        f"The dominant emotion is"
        f"<strong>{response['dominant_emotion']} </strong>"
    )


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
