import flet as ft

# Данные
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

# Создание приложения
def main(page: ft.Page):
    page.title = "Cryptocurrency Aggregator"
    page.theme_mode = ft.ThemeMode.DARK
    page.background_color = ft.colors.BLACK
    page.padding = 20

    # Заголовок
    page.add(ft.Text(value="Cryptocurrency Aggregator", size=24, weight="bold", color=ft.colors.WHITE, align=ft.Alignment.CENTER))

    # Таблица
    table = ft.DataTable(
        border_color=ft.colors.WHITE,
        columns=[
            ft.DataColumn(ft.Text("", color=ft.colors.WHITE))  # Пустой заголовок для первого столбца
        ] + [ft.DataColumn(ft.Text(exchange, color=ft.colors.WHITE)) for exchange in exchanges],
        rows=[]
    )

    # Заполнение таблицы
    for coin in coins:
        cells = [ft.DataCell(ft.Text(coin, color=ft.colors.WHITE))]
        for exchange in exchanges:
            cell = ft.DataCell(ft.Text("", color=ft.colors.WHITE))
            cells.append(cell)
        table.rows.append(ft.DataRow(cells=cells))

    page.add(table)

    # Функция для обновления процентных ставок
    def update_staking_rate(coin, exchange, rate):
        for row in table.rows:
            if row.cells[0].content.value == coin:
                for cell in row.cells[1:]:
                    if cell.content.value == exchange:
                        cell.content.value = rate
                        page.update()

    # Пример обновления процентной ставки
    update_staking_rate("BTC", "Binance", "5.0%")

# Запуск приложения
ft.app(target=main)
