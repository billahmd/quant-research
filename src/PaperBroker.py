class PaperBroker:

    def __init__(self, initial_cash):
        self.cash = initial_cash
        self.postions = {}
        self.trades = []

        def get_position(self, symbol)
            return self.positions.get(symbol, 0)
        def buy(self, symbol, price, quantity):
            cost = price * quantity

            if cost > self.cash:
                print("Not enough cash")
                return
            self.cash -= cost
            self.positions[symbol] = self.get_postion(symbol) + quantity
            self.trades.append({
                "side": "BUY",
                "symbol": symbol,
                "price": price,
                "quantity": quantity
            })
        def sell(self, symbol, price, quantity):
            current_position = self.get_position(symbol)

            if quantity > current_position:
                print("Not enough shares to sell")
                return

            self.cash += price * quantity
            self.positions[symbol] = current_position - quantity

            self.trades.append({
                "side": "SELL",
                "symbol": symbol,
                "price": price,
                "quantity": quantity
            })