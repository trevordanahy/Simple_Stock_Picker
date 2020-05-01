def stock_picker(stock_prices):
	reverse_prices = stock_prices[::-1]

	profit_max = [0,0]
	profit = 0

	for buy in stock_prices:
		for sell in reverse_prices:
			if stock_prices.index(sell) <= stock_prices.index(buy):
				continue
			elif (sell-buy) > profit:
				profit = sell - buy
				profit_max[0] = stock_prices.index(buy)
				profit_max[1] = stock_prices.index(sell)
			else:
				continue
	return profit_max







