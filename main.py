from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual Alpaca keys
ALPACA_KEY_ID = 'PKSOB352J0MW1TOIECD6'
ALPACA_SECRET_KEY = 'hujr7cgZERs0NYSCzHYBvF5sHDEQxXFJK872UC4y'

@app.route('/alpaca/account', methods=['GET'])
def proxy_account():
    _ = request.headers.get("X-API-KEY")  # Optional: placeholder for ChatGPT token

    headers = {
        'APCA-API-KEY-ID': ALPACA_KEY_ID,
        'APCA-API-SECRET-KEY': ALPACA_SECRET_KEY
    }

    response = requests.get('https://paper-api.alpaca.markets/v2/account', headers=headers)

    if response.status_code != 200:
        return jsonify({"error": "Failed to retrieve account"}), response.status_code

    data = response.json()

    # Helper to safely convert strings to floats
    def safe_float(value):
        try:
            return float(value)
        except (TypeError, ValueError):
            return 0.0

    cleaned = {
        "account_number": data.get("account_number"),
        "status": data.get("status"),
        "currency": data.get("currency"),
        "cash": safe_float(data.get("cash")),
        "equity": safe_float(data.get("equity")),
        "buying_power": safe_float(data.get("buying_power")),
        "portfolio_value": safe_float(data.get("portfolio_value"))
    }

    return jsonify(cleaned), 200

@app.route('/')
def home():
    return '✅ Alpaca Proxy is running!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
