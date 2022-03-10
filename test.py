# -*- coding: utf-8 -*-
from data import actions, sold
from prettytable import PrettyTable
from math import floor,ceil
import time
import csv


class AlgoInvestTrade:
	def __init__(self, amount, filename):
		self.amount = amount
		self.filename = filename

	def serializer(self, filename):
		shares = []
		with open(f'{filename}.csv', newline='') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
			for row in spamreader:
				share = ', '.join(row).split(",")
				if share[0] != 'name' and float(share[1])>0.0:
					price = round(float(share[1]),2)
					profit = round(float(share[2]),2)
					shares.append({"share":share[0], "price": price, "profit":profit})
		new_shares = sorted(shares, key=lambda d: d['price'])
		return new_shares

	def combinations(self,shares):
		amount = self.amount
		n = len(shares)
		table = [[0 for x in range(amount + 1)] for x in range(n + 1)]
		for i in range(n + 1):
			for w in range(amount + 1):
				if i == 0 or w == 0:
					table[i][w] = 0
				elif ceil(shares[i-1]['price'])<= w:
					reward = shares[i-1]['price']+(shares[i-1]['price']*shares[i-1]['profit']/100)
					table[i][w] = max(reward + table[i-1][w-ceil(shares[i-1]['price'])], table[i-1][w])
				else:
					table[i][w] = table[i-1][w]
		print(table[n][w])
		return table
	
	def portfolio(self, table, shares):
		n, amount, total_price,profit = len(shares),self.amount,0,0
		portfolio = []
		while amount >=0 and n>=0:
			share = shares[n-1]
			reward = share['price']+share['price']*share['profit']/100
			if table[n][amount] == table[n-1][amount-ceil(share['price'])]+reward:
				portfolio.append(share)
				amount -= ceil(share['price'])
				profit = profit + reward
				total_price = total_price + share['price']
			n -=1
		percentage = (profit-self.amount)/self.amount*100
		return {"shares": portfolio, "total_price": total_price, 
				"yields":profit, "percentage": percentage}


	def display(self, portfolio):
		shares = []
		t = PrettyTable(['share', 'price', 'APY in 2 years', 'reward'])
		for share in portfolio['shares']:
			yield_ = share['price']+share['price']*share['profit']/100
			s = [share['share'], share['price'], share['profit'], round(yield_, 2)]
			shares.append(s)
		for share in shares:
			t.add_row(share)
		t.add_row(['Total cost',round(portfolio['total_price'], 2), 
			round(portfolio['percentage'], 2),round(portfolio['yields'], 2)])
		print(f"SOLDE DEPART : {self.amount}E")
		print(t.get_string(title="AlgoInvest&Trade"))

	def main(self):
		shares = self.serializer(self.filename)
		table = self.combinations(shares)
		portfolio = self.portfolio(table, shares)
		self.display(portfolio)


if __name__ == '__main__':
	start_time = time.time()
	amount = 500
	filename = 'dataset0'
	algoInvestTrade = AlgoInvestTrade(amount, filename)
	algoInvestTrade.main()
	print("--- %s seconds ---" % (time.time() - start_time))