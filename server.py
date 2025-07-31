"""Flask server module for Emotion Detection App."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Create the Flask app
app = Flask("Emotion Detector")

# Route to handle emotion detection
@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Handles emotion detection requests from the front-end."""
    # Retrieve text from query parameter
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)

    # Handle invalid results
    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    # Format the response message
    response_msg = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_msg

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=50002)
