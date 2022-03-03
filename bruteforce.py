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

	def check_other_elem_can_add(self, group, total_cost):
		for action in self.actions:
			action_not_in_group = self.check_action_not_in_group(action, group)
			if total_cost + int(action['cout']) < self.sold and action_not_in_group:
				return True
		return False

	def create_combinations(self, combinations, actions):
		max_yields = 0
		list_next_level_combinations = []
		copy_combination = []
		print(f"nb combinations {len(combinations)}")
		for combination in combinations:
			for action in actions:
				copy_combination = [c for c in combination]
				if self.check_action_not_in_group(action, combination):
					copy_combination.append(action)
					total_cost = self.calculate_cost(copy_combination)
					if total_cost < self.sold:
						list_next_level_combinations.append(copy_combination)
					else:
						if self.check_other_elem_can_add(combination, total_cost):
							list_next_level_combinations.append(combination)
						else:
							yields = self.calculate_yields(combination)
							if yields > max_yields:
								max_yields = yields
								print({"yields": max_yields})
								print({"actions": combination})
				else:
					list_next_level_combinations.append(combination)
		return list_next_level_combinations

	def call_next_combinations(self, combinations):
		for i in range(len(self.actions)):
			combinations = self.create_combinations(combinations, self.actions)

	def main_combination(self):
		for index in range(len(self.actions)):
			first_combinations = [[self.actions[index]] for i in range(len(self.actions))]
			print(f"{self.actions[index]}")
			self.call_next_combinations(first_combinations)

	def main(self):
		actions = self.actions
		max_yields = 0

		for current in range(len(actions)):
			group_actions = [[a] for a in self.actions]
			group_actions_bis = []
			print(f"action index : {current}")
			for action in actions:
				for group in group_actions:
					if self.check_action_not_in_group(action, group):
						group.append(action)
						total_cost = self.calculate_cost(group)
						if total_cost < self.sold:
							group_actions_bis.append(group)
						else:
							group.pop(-1)
							if self.check_other_elem_can_add(group, total_cost):	
								group_actions_bis.append(group)
							else:
								yields = self.calculate_yields(group)
								if yields > max_yields:
									max_yields = yields
									print({"yields": max_yields})
					else:
						group_actions_bis.append(group)
				group_actions = [grp for grp in group_actions_bis]
			index = actions.pop(0)
			actions.append(index)
		print({"actions":f"{group}", "yields": max_yields})


if __name__ == '__main__':
	bf = BruteForce(actions, sold)
	#bf.main()
	bf.main_combination()
		