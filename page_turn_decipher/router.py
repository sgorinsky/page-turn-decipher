from flask import Flask, request
import pickle
import sklearn
from page_turn_decipher.utils.clean_text import clean_text
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/health')
def health():
    return 'success', 200

@app.route('/prediction', methods=["GET", "POST"])
def make_prediction():
    """Ingest text data, clean+vectorize, return prediction
    """
    
    body = request.form # serialized string
    text = body['text']
    
    model = pickle.load(open('static/model.pkl', 'rb'))
    prediction = model.predict([clean_text(text)])
    return {
        'data': {
            'is_real': bool(prediction[0])
        }
    }
    
    
    

