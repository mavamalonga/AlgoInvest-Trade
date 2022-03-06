from data import actions, sold
from math import floor

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
	print(K[n][w])
	w = W # k > W
	n = len(actions) #len(shares_list)
	portfolio = []
	somme = 0
	rew_sum = 0
	while w >=0 and n>=0:
		share = actions[n-1]
		reward = int(share['cout'])+int(share['cout'])*int(share['benefice'])/100
		if K[n][floor(w)] == K[n-1][floor(w)-int(share['cout'])]+reward:
			portfolio.append(share)
			w -= int(share['cout'])
			rew_sum = rew_sum + int(share['cout'])+int(share['cout'])*int(share['benefice'])/100
			somme = somme + int(share['cout'])
		n -=1
	print(somme)
	print(rew_sum)
	return portfolio


if __name__ == '__main__':
	W = sold
	wt = actions
	val = actions
	n = len(actions)
	print(knapSack(W, wt, val, n))