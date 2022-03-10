# -*- coding: utf-8 -*-
from prettytable import PrettyTable
from math import floor,ceil
from bruteforce import BruteForce
from optimized import Dynamic_Approach
import time
import csv

if __name__ == '__main__':
	start_time = time.time()
	amount = 500
	filename = 'dataset2'
	algoInvestTrade = Dynamic_Approach(amount, filename)
	algoInvestTrade.main()
	print("--- %s seconds ---" % (time.time() - start_time))