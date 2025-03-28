# from flask import Flask, request
# import threading
# from src.main import main
# import os
# import requests


# app = Flask(__name__)


# @app.route('/', methods=['POST', 'GET'])
# def webhook():

#     try:
#         data = request.json
#         print("Webhook receive:", data)

#         threading.Thread(target = main, args=(
#             "avisos",
#             "page1",
#             3
#         )).start()
#     except: NameError
#     return {"status": "OK"}, 200



# if __name__ == '__main__':
#     port = int(os.env.get("PORT", 5000))
#     app.run(host="0.0.0.0", port=port, debug=True)