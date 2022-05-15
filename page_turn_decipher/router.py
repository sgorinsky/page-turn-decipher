from flask import Flask
from page_turn_decipher.utils.clean_text import clean_text
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/health')
def health():
    return 'success', 200

@app.route('/prediction')
def make_prediction():
    """Ingest text data, clean+vectorize, return prediction
    """
    
    text_request = request.body # serialized string
    text = str(text_request)
    cleaned_text = clean_text(text)
    
    # load ml model and make prediction below
    pass
    
    

