from page_turn_decipher.router import app
from waitress import serve

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
