from data import actions, sold
import yaml
import json


class BruteForce:
	def __init__(self, actions, sold):
		self.actions = actions
		self.sold = sold

	def calculate_cost(self, group):
		total_cost = 0
		for action in group:
			total_cost = total_cost + int(action['cout'])
		return total_cost

	def calculate_yields(self, groups):
		yields = 0
		for action in groups:
			yields = yields + int(action['cout']) + int(action['cout'])*(int(action['benefice'])/100)
		return yields

	def check_action_not_in_group(self, action, group):
		return action not in group

	def main(self):
		actions = self.actions
		max_yields = 0
		group_actions_bis = []

		for current in range(len(actions)):
			group_actions = [[a] for a in self.actions]
			for action in actions:
				for group in group_actions:
					action_not_in_group = self.check_action_not_in_group(action, group)
					if action_not_in_group:
						group.append(action)
						total_cost = self.calculate_cost(group)
						if total_cost < self.sold:
							group_actions_bis.append(group)
						else:
							group.pop(-1)
							group_actions_bis.append(group)
							yields = self.calculate_yields(group)
							if yields > max_yields:
								max_yields = yields
					else:
						group_actions_bis.append(group)
				group_actions = [group for group in group_actions_bis]
			index = actions.pop(0)
			actions.append(index)
		return {"actions": group, "yields": max_yields}


if __name__ == '__main__':
	bf = BruteForce(actions, sold)
	max_yield = bf.main()
	print(max_yield)
		