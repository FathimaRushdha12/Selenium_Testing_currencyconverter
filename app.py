import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

API_KEY = 'YOUR_EXCHANGERATE_API_KEY'

def convert_currency(from_currency, to_currency, amount):
    url = f'https://v6.exchangeratesapi.io/latest?base={from_currency}&symbols={to_currency}'
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if to_currency in data['rates']:
            exchange_rate = data['rates'][to_currency]
            converted_amount = amount * exchange_rate
            return converted_amount
        else:
            return None
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.json
        amount = float(data['amount'])
        from_currency = data['from_currency']
        to_currency = data['to_currency']
        converted_amount = convert_currency(from_currency, to_currency, amount)
        if converted_amount is not None:
            return jsonify({'result': converted_amount})
        else:
            return jsonify({'error': 'Failed to retrieve exchange rate'}), 500
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
