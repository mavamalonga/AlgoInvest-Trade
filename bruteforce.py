from data import actions, sold


class BruteForce:
	def __init__(self, actions, sold):
		self.actions = actions
		self.sold = sold

	def calculate_cost(self, group_action):
		total_cost = 0
		actions_number = group_action.split("$")
		for nb in actions_number:
			for action in self.actions:
				if action['action'] == f'action-{nb}':
					total_cost = total_cost + int(action['cout'])
		return total_cost

	def calculate_yields(self, group_action):
		numbers = group_action.split("$")
		yields = 0
		for nb in numbers:
			for action in self.actions:
				if action['action'] == f'action-{nb}':
					yields = yields + int(action['cout']) + int(action['cout'])*(int(action['benefice'])/100)
		return yields

	def check_action_not_in_group(self, new_action, group_action):
		actions_number = group_action.split("$")
		return new_action not in actions_number

	def main(self):
		actions = self.actions
		max_yields = 0
		group_actions_bis = []

		for current in range(len(actions)):
			index = actions.pop(0)
			actions.append(index)
			group_actions = [a['action'][7:] for a in self.actions]
			for action in actions:
				for group in group_actions:
					action_not_in_group = self.check_action_not_in_group(action['action'][7:], group)
					if action_not_in_group:
						new_group = group + "$" + action['action'][7:]
						total_cost = self.calculate_cost(new_group)
						if total_cost < self.sold:
							new_group = group + "$" + action['action'][7:]
							group_actions_bis.append(new_group)
						else:
							group_actions_bis.append(group)
							yields = self.calculate_yields(group)
							if yields > max_yields:
								max_yields = yields
								print({"group_actions": group, "yields_max": max_yields})
				group_actions = [group for group in group_actions_bis]


if __name__ == '__main__':
	bf = BruteForce(actions, sold)
	bf.main()
		