'''Module to handle emotion detection'''
from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route("/emotionDetector")
def emo_detector():
    '''
    Takes text input and finds the emotion in the text
    '''
    text_to_analyze = request.args.get('data')
    res = emotion_detector(text_to_analyze)
    if res.dominant_emotion is None:
        return "Invalid text! Please try again!."
    return f'''For the given statement,
    the system response is 'anger': {res['anger']}, 'disgust': {res['disgust']}, 'fear': {res['fear']}, 'joy': {res['joy']} and 'sadness': {res['sadness']}. 
    The dominant emotion is {res['dominant_emotion']}.'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
