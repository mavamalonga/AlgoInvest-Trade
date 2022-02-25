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

	def calculate_group_actions_cost(self, group_action):
		total_cost = 0
		actions_number = group_action.split("$")
		for nb in actions_number:
			for action in self.actions:
				if action['action'] == f'action-{nb}':
					total_cost = total_cost + int(action['cout'])
		return total_cost

	def calculate_yields(self, group_action):
		actions_number = group_action.split("$")
		yields = 0
		for nb in actions_number:
			for action in self.actions:
				if action['action'] == f'action-{nb}':
					yields = yields + int(action['cout']) + int(action['cout'])*(int(action['benefice'])/100)
		return yields

	def action_not_in_group(self, new_action, group_action):
		actions_number = group_action.split("$")
		return new_action not in actions_number

	def algo_brute_force(self):
		your_list = self.actions
		complete_list = []
		max_yields = 0
		a_bis = []
		for current in range(len(your_list)):
			i_index = your_list.pop(0)
			your_list.append(i_index)
			a = [i['action'][7:] for i in self.actions]
			e=0
			for i in your_list:
				for x in a:
					action_not_in = self.action_not_in_group(i['action'][7:], x)
					if action_not_in:
						add_new_action = i['action'][7:]+ "$" + x
						total_cost = self.calculate_group_actions_cost(add_new_action)
						if total_cost < 500:
							val = i['action'][7:]+ "$" + x
							a_bis.append(val)
						else:
							val = x
							a_bis.append(val)
							yields = self.calculate_yields(x)
							if yields > max_yields:
								max_yields = yields
								print({"group_actions": val, "yields_max": max_yields,})
				e = e + 1
				print(f"tour : {e}")
				a = [c for c in a_bis]
			print(f"all for {i}")
			exit()
			#complete_list = complete_list+a

	def main(self):
		self.algo_brute_force()


if __name__ == '__main__':
	bf = BruteForce(actions, sold)
	bf.main()
		