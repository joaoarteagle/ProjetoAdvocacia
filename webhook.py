from flask import Flask, request
import threading
from main import main
from pyngrok import ngrok, conf, installer


app = Flask(__name__)

@app.route('/webhook', methods=['POST', 'PUT'])
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