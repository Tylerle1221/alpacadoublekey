from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ALPACA_KEY_ID = 'PKSOB352J0MW1TOIECD6'
ALPACA_SECRET_KEY = 'hujr7cgZERs0NYSCzHYBvF5sHDEQxXFJK872UC4y'

@app.route('/alpaca/account', methods=['GET'])
def proxy_account():
    _ = request.headers.get("X-API-KEY")  # Optional dummy for ChatGPT
    _ = request.headers.get("X-API-KEY")  # Dummy header to accept ChatGPT's token

    headers = {
        'APCA-API-KEY-ID': ALPACA_KEY_ID,
@@ -23,7 +23,6 @@

    data = response.json()

    # Safely cast money fields to float
    def safe_float(value):
        try:
            return float(value)
@@ -41,12 +40,3 @@
    }

    return jsonify(cleaned), 200

@app.route('/')
def home():
    return '✅ Alpaca Proxy is running!'

if __name__ == '__main__':
    # Required for Render to detect the port
    app.run(host='0.0.0.0', port=10000)
