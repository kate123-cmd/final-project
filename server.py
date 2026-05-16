"""
Executing this function initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on
localhost:5000.
"""

# Import Flask, render_template, request from the flask package
from flask import Flask, render_template, request

# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emot_detector():
    """
    Analyze the provided text and return detected emotions.
    """

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function
    response = emotion_detector(text_to_analyze)

    # Check for invalid/blank input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is "
        f"{response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    Render the main application page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
