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
			if self.check_actions_purchased(actions_purchased) == False:
				if self.check_sold(action):
					yields = self.calculate_yields(action)
					actions_purchased.append(action)

	def try_all_possibilities_for_value(self):
		list_buy_actions = []
		max_yields = []
		for action in self.actions:
			self.buy_actions(list_buy_actions)

	def main(self):
		self.try_all_possibilities_for_value()


if __name__ == '__main__':
	bf = BruteForce(actions, sold)
	bf.main()
		