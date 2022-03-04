from itertools import combinations
from tabulate import tabulate
from prettytable import PrettyTable
from data import actions, sold


class BruteForce:
	def __init__(self, actions, sold):
		self.actions = actions
		self.sold = sold

	def calculate_cost(self, group):
		total_cost = 0
		for action in group:
			total_cost = total_cost + int(action['cout'])
		return total_cost

	def calculate_yield(self, groups):
		profit = 0
		percentage = 0
		for action in groups:
			profit = profit + int(action['cout']) + int(action['cout'])*(int(action['benefice'])/100)
		return profit

	def combinations(self, iterable, r):
	    # combinations('ABCD', 2) --> AB AC AD BC BD CD
	    # combinations(range(4), 3) --> 012 013 023 123
	    pool = tuple(iterable)
	    n = len(pool)
	    if r > n:
	        return
	    indices = list(range(r))
	    yield tuple(pool[i] for i in indices)
	    while True:
	        for i in reversed(range(r)):
	            if indices[i] != i + n - r:
	                break
	        else:
	            return
	        indices[i] += 1
	        for j in range(i+1, r):
	            indices[j] = indices[j-1] + 1
	        yield tuple(pool[i] for i in indices)

	def display_result(self, combination):
		t = PrettyTable(['Action', 'Coût', 'Rendement (APY)', 'Profits après 2 ans'])
		actions = [[action['action'], action['cout']+"€", 
			action['benefice']+"%", None] for action in combination['combination']]
		for action in actions:
			t.add_row(action)
		t.add_row(['Total',str(round(combination['total_cost'], 2))+"€", 
			str(round(combination['percentage'], 2))+"%",str(round(combination['yields'], 2))+"€"])
		print(t.get_string(title="AlgoInvest&Trade"))


	def main(self):
		max_profit = 0
		for size_combinations in range(len(self.actions)+1):
			if size_combinations > 0:
				combinations = list(self.combinations(self.actions, size_combinations))
				for combination in combinations:
					total_cost = self.calculate_cost(combination)
					profit = self.calculate_yield(combination)
					if total_cost < self.sold and profit > max_profit:
						max_profit = profit
						percentage = (profit-self.sold)/self.sold*100
						best_combination = {"combination": combination, 
							"total_cost": total_cost, "yields":max_profit, "percentage": percentage}
		self.display_result(best_combination)

					
if __name__ == '__main__':
	bruteforce = BruteForce(actions, sold)
	bruteforce.main()
		