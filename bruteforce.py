from data import actions, sold


class BruteForce:
	def __init__(self, actions, solde):
		self.actions = actions
		self.sold = sold

	def order_by_cost(self):
		shares_order = sorted(self.shares, key=lambda k: int(k['cout']))
		return actions_order

	def check_sold(self, action):
		if self.sold > int(action['cout']):
			self.sold = self.sold - int(action['cout'])
			return True
		return False

	def calculate_yields(self, action):
		yields = int(action['cout']) + int(action['cout'])*(int(action['benefice'])/100)
		return yields

	def check_actions_purchased(self, action, actions_purchased):
		for action_purchased in actions_purchased:
			if action['action'] == actions_purchased['action']:
				return True
			return False

	def buy_actions(self):
		for action in self.action:
			if self.check_actions_purchased(complete_list) == False:
				if self.check_sold(action):
					yields = self.calculate_yields(action)
					actions_purchased.append(action)

	def try_all_possibilities_for_value(self):
		your_list = 'abcd'
		complete_list = []
		for current in range(4):
			a = [i for i in your_list]
			for y in range(current):
				a = [x+i for i in your_list for x in a if i not in x]
			complete_list = complete_list+a
		print(complete_list)

	def algo_brute_force(self):
		your_list = self.actions
		complete_list = []
		propositions = []
		a_bis = []

		for current in range(len(your_list)):
			i_index = your_list.pop(0)
			your_list.append(i_index)
			a = [i['action'][7:] for i in self.actions]
			for i in your_list:
				for x in a:
					val = i['action'][7:]+ "$" + x
					a_bis.append(val)
				a = [c for c in a_bis]
				print(a)
				exit()
			#complete_list = complete_list+a

	def main(self):
		self.algo_brute_force()


if __name__ == '__main__':
	bf = BruteForce(actions, sold)
	bf.main()
		