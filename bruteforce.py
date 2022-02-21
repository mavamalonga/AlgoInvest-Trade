# bruteforce


actions = [
	{"action":"action-1", "cout":"20", "benefice":"5"},
	{"action":"action-2", "cout":"30", "benefice":"10"},
	{"action":"action-3", "cout":"50", "benefice":"15"},
	{"action":"action-4", "cout":"70", "benefice":"20"},
	{"action":"action-5", "cout":"60", "benefice":"17"},
	{"action":"action-6", "cout":"80", "benefice":"25"},
	{"action":"action-7", "cout":"22", "benefice":"7"},
	{"action":"action-8", "cout":"26", "benefice":"11"},
	{"action":"action-9", "cout":"48", "benefice":"13"},
	{"action":"action-10", "cout":"34", "benefice":"27"},
	{"action":"action-11", "cout":"42", "benefice":"17"},
	{"action":"action-12", "cout":"110", "benefice":"9"},
	{"action":"action-13", "cout":"38", "benefice":"23"},
	{"action":"action-14", "cout":"14", "benefice":"1"}, 
	{"action":"action-15", "cout":"18", "benefice":"3"},
	{"action":"action-16", "cout":"08", "benefice":"8"},
	{"action":"action-17", "cout":"04", "benefice":"12"},
	{"action":"action-18", "cout":"10", "benefice":"14"},
	{"action":"action-19", "cout":"24", "benefice":"21"},
	{"action":"action-20", "cout":"114", "benefice":"18"}
]

sold = 500

class RentAlgo:
	def __init__(self, shares, sold):
		self.sold = sold
		self.shares = shares

	def select_shares(self):
		shares_selected = []
		for share in self.shares:
			while self.sold > int(share['cout']):
				self.sold = self.sold -int(share['cout'])
				shares_selected.append(share)
		return shares_selected

	def yields(self, shares_selected):
		# yields in 2 years with a starting bid of 500$
		total_yields = 0
		for share in shares_selected:
			share_yield_2_years = int(share['cout']) + int(share['cout'])*(int(share['benefice'])/100)
			total_yields = total_yields + share_yield_2_years
		return total_yields

	def main(self):
		shares_selected = self.select_shares()
		total_yields = self.yields(shares_selected)
		return total_yields

rentAlgo = RentAlgo(actions, sold)
yields_in_2_years = rentAlgo.main()
print(yields_in_2_years)