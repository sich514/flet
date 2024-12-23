import flet as ft

# Список монет и бирж
coins = [
    "BTC", "USDT", "ETH", "USDC", "ATOM", "XRP", "XLM", "UNI", "TRX", "SOL", "SHIB", "NEAR", "LTC",
    "LINK", "ETC", "EOS", "DOT", "DOGE", "BCH", "AVAX", "APE", "ADA", "OP", "ARB", "POL", "AXS",
    "ASTR", "ENA", "JUP", "DAI", "INJ", "APT", "FLOKI", "KAVA", "REZ", "MANA", "TAO", "ZEC", "ACE", "IO",
    "FLOW", "BB", "FIL", "SEI", "DYM", "DYDX", "ICP", "STORJ", "AEVO", "STRK", "MKR", "ETHFI", "NOT", "ZETA",
    "GRT", "SUI", "AI", "W", "ZK", "PEOPLE", "CHZ", "HBAR", "FTM", "AAVE", "BOME", "TON", "MANTA", "TRB", "ARKM",
    "CRV", "LDO", "SUSHI", "SNX", "OMNI", "THETA", "AR", "SAND", "PENDLE", "ALGO", "RUNE", "GALA", "MEME", "JASMY",
    "ZRO", "WIF", "BONK", "PEPE", "USDE", "BWB", "DOT", "BWB", "CORE", "ONDO", "TIA", "BGB", "EIGEN", "LUNA", "BNB", "LUNC"
]

exchanges = ["Binance", "Bitget", "Mexc", "Gate", "Okx", "Whitebit"]

# Инициализация ставок
rates = {coin: {exchange: "" for exchange in exchanges} for coin in coins}

def main(page: ft.Page):
    page.title = "Crypto Rates Table"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "always"

    def update_rate(coin, exchange, value):
        rates[coin][exchange] = value
        page.update()

    # Заголовок таблицы
    header_row = [
        ft.Text("Монета / Биржа", weight="bold", size=14, width=120, color="white")
    ]
    header_row.extend(
        ft.Text(exchange, weight="bold", size=14, width=120, color="white") for exchange in exchanges
    )

    # Генерация строк таблицы
    table_rows = []
    for coin in coins:
        row = [
            ft.Text(coin, weight="bold", size=12, width=120, color="white")
        ]
        for exchange in exchanges:
            rate_input = ft.TextField(
                hint_text="%",
                width=120,
                height=30,
                value=rates[coin][exchange],
                on_change=lambda e, c=coin, ex=exchange: update_rate(c, ex, e.control.value),
            )
            row.append(rate_input)
        table_rows.append(ft.Row(row))

    # Основное содержимое
    content = ft.Column([
        ft.Row(header_row, alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(color="white"),
        *table_rows,
    ])

    page.add(ft.Container(content, padding=20, bgcolor="black"))

ft.app(target=main)
