from data import actions, sold
# a dynamic approach
# Returns the maximum value that can be stored by the bag
def knapSack(W, wt, val, n):
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
	return K[n][W]
"""
#Main
val = [50,100,150,200,10] #un tableau de valeurs qui contient la valeur de tous les éléments <=>RENDEMENT
wt = [8,16,32,40,10] #nous avons un tableau de poids qui contient le poids de tous les éléments <=> COUT
W = 74 #nous avons une capacité de poids totale du sac à dos <=> SOLDE 
n = len(val)
print(knapSack(W, wt, val, n))
"""
W = sold
wt = actions
val = actions
n = len(actions)
print(knapSack(W, wt, val, n))
