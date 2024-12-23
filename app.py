from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Данные для монет и бирж
coins = ["BTC", "USDT", "ETH", "USDC", "ATOM", "XRP", "XLM", "UNI", "TRX", "SOL",
         "SHIB", "NEAR", "LTC", "LINK", "ETC", "EOS", "DOT", "DOGE", "BCH",
         "AVAX", "APE", "ADA", "OP", "ARB", "POL", "AXS", "ASTR", "ENA",
         "JUP", "DAI", "INJ", "APT", "FLOKI", "KAVA", "REZ", "MANA", "TAO",
         "ZEC", "ACE", "IO", "FLOW", "BB", "FIL", "SEI", "DYM", "DYDX",
         "ICP", "STORJ", "AEVO", "STRK", "MKR", "ETHFI", "NOT", "ZETA", "GRT",
         "SUI", "AI", "W", "ZK", "PEOPLE", "CHZ", "HBAR", "FTM", "AAVE", "BOME",
         "TON", "MANTA", "TRB", "ARKM", "CRV", "LDO", "SUSHI", "SNX", "OMNI",
         "THETA", "AR", "SAND", "PENDLE", "ALGO", "RUNE", "GALA", "MEME",
         "JASMY", "ZRO", "WIF", "BONK", "PEPE", "USDE", "BWB", "CORE", "ONDO",
         "TIA", "BGB", "EIGEN", "LUNA", "BNB", "LUNC"]

exchanges = ["Binance", "Bitget", "Mexc", "Gate", "Okx", "Whitebit"]

# Хранение процентных ставок
staking_rates = {coin: {exchange: "" for exchange in exchanges} for coin in coins}

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            coin = request.form['coin']
            exchange = request.form['exchange']
            rate = request.form['rate']
            staking_rates[coin][exchange] = rate
            return redirect(url_for('index'))
        return render_template('index.html', coins=coins, exchanges=exchanges, staking_rates=staking_rates)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)
