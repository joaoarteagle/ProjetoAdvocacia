from flask import Flask, request
import threading
from src.main import main



app = Flask(__name__)

@app.route('/', methods=['POST', 'PUT', 'GET'])
def webhook():
    data = request.json
    print("Webhook receive:", data)

    threading.Thread(target = main, args=(
        "avisos",
        "page1",
        3
    )).start()

    return {"status": "OK"}, 200



if __name__ == '__main__':
    app.run(port=5000, debug=True)