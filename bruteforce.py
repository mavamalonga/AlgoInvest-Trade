from data import actions, sold

class RentAlgo:
	def __init__(self, shares, sold):
		self.init_sold = sold
		self.shares = shares
		self.share_demo = {"action":"action-default", "cout":"20", "benefice":"5"}

	def order_by_cost_reverse(self):
		shares_order = sorted(self.shares, key=lambda k: int(k['cout']), reverse=True)
		return shares_order

	def select_shares(self, shares, share_removed, sold):
		shares_selected = []
		for share in shares:
			if sold > int(share['cout']) and share_removed['action'] != share['action']:
				sold = sold -int(share['cout'])
				shares_selected.append(share)
		return shares_selected, sold

	def calculate_yields(self, shares_selected):
		total_yields = 0
		for share in shares_selected:
			share_yield_2_years = int(share['cout']) + int(share['cout'])*(int(share['benefice'])/100)
			total_yields = total_yields + share_yield_2_years
		return total_yields

	def main(self):
		list_total_yields = []
		top_total_yield = 0
		min_total_yield = 0
		first_turn = True
		shares_order = self.order_by_cost_reverse()
		for share_removed in shares_order:
			if first_turn:
				sold = self.init_sold
				share_removed = self.share_demo
				shares_selected, sold_staying = self.select_shares(shares_order, share_removed, sold)
				total_yields = self.calculate_yields(shares_selected)
				list_total_yields.append(total_yields)
			else:
				sold = self.init_sold
				shares_selected, sold_staying = self.select_shares(shares_order, share_removed, sold)
				total_yields = self.calculate_yields(shares_selected)
				list_total_yields.append(total_yields)
			first_turn = False

		print(f"{list_total_yields}")

rentAlgo = RentAlgo(actions, sold)
yields_in_2_years = rentAlgo.main()