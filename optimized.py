# -*- coding: utf-8 -*-
from data import actions, sold
from math import floor
from prettytable import PrettyTable
import time


class AlgoInvestTrade:
	def __init__(self, deposit, shares):
		self.deposit = deposit
		self.shares = shares
		self.len_shares = len(shares)

	def knapSack(self, W, wt, val, n):
		K = [[0 for x in range(W + 1)] for x in range(n + 1)]
		#Table in bottom up manner
		for i in range(n + 1):
			for w in range(W + 1):
				if i == 0 or w == 0:
					K[i][w] = 0
				elif int(wt[i-1]['cout']) <= w:
					reward = int(val[i-1]['cout'])+int(val[i-1]['cout'])*int(val[i-1]['benefice'])/100
					K[i][w] = max(reward + K[i-1][w-int(wt[i-1]['cout'])],  K[i-1][w])
				else:
					K[i][w] = K[i-1][w]
		return K[n][w], K
	
	def make_portfolio(self, table):
		K = table
		n = self.len_shares
		w = self.deposit
		portfolio = []
		total_cost = 0
		profit = 0
		while w >=0 and n>=0:
			share = actions[n-1]
			reward = int(share['cout'])+int(share['cout'])*int(share['benefice'])/100
			if K[n][floor(w)] == K[n-1][floor(w)-int(share['cout'])]+reward:
				portfolio.append(share)
				w -= int(share['cout'])
				profit = profit + int(share['cout'])+int(share['cout'])*int(share['benefice'])/100
				total_cost = total_cost + int(share['cout'])
			n -=1
		percentage = (profit-self.deposit)/self.deposit*100
		portfolio = {"combination": portfolio, "total_cost": total_cost, "yields":profit, "percentage": percentage}
		return portfolio

	def display_result(self, combination):
		t = PrettyTable(['share', 'Cost', 'percentage yields in 2 years', 'Profit 2 years after'])
		actions = [[action['action'], action['cout']+"E", action['benefice']+"%", 
		str(round(float(float(action['cout'])))+(float(action['cout'])*(float(action['benefice'])/100)))+"E"] \
		for action in combination['combination']]
		for action in actions:
			t.add_row(action)
		t.add_row(['Total',str(round(combination['total_cost'], 2))+"E", 
			str(round(combination['percentage'], 2))+"%",str(round(combination['yields'], 2))+"E"])
		print(f"SOLDE DEPART : {self.deposit}E")
		print(t.get_string(title="AlgoInvest&Trade"))

	def main(self):
		max_rewards, table = self.knapSack(self.deposit, self.shares, self.shares, self.len_shares)
		portfolio = self.make_portfolio(table)
		self.display_result(portfolio)


if __name__ == '__main__':
	start_time = time.time()
	deposit = sold
	shares = actions
	invest = AlgoInvestTrade(deposit, shares)
	invest.main()
	print("--- %s seconds ---" % (time.time() - start_time))