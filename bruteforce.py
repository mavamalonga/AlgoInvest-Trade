# -*- coding: utf-8 -*-
from prettytable import PrettyTable
import time
import csv


class BruteForce:
    def __init__(self, amount, filename):
        self.amount = amount
        self.filename = filename

    def serializer(self, filename):
        shares = []
        file = "csv/%s.csv" % (filename)
        with open(file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                share = ', '.join(row).split(",")
                if share[0] != 'name' and float(share[1]) > 0.0:
                    shares.append({"share": share[0], "price": float(share[1]),
                                   "profit": float(share[2])})
        new_shares = sorted(shares, key=lambda d: d['price'])
        return new_shares

    def calculate_cost_and_profit(self, shares):
        cost, profit = 0, 0
        for share in shares:
            cost += share['price']
            profit += share['price']+share['price']*share['profit']/100
        return cost, profit

    def combinations(self, iterable, r):
        pool = tuple(iterable)
        n = len(pool)
        if r > n:
            return
        indices = list(range(r))
        yield tuple(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i+1, r):
                indices[j] = indices[j-1] + 1
            yield tuple(pool[i] for i in indices)

    def portfolio(self, shares, cost, profit):
        pnl = profit - cost
        sum_total = profit + (self.amount-cost)
        return {"shares": shares, "cost": cost, "return": pnl, "sum": sum_total}

    def display(self, portfolio):
        shares = []
        t = PrettyTable(['share', 'price($)', 'yield(%)', 'benefit($)'])
        for share in portfolio['shares']:
            benef = share['price']*share['profit']/100
            s = [share['share'], share['price'], share['profit'], round(benef, 2)]
            shares.append(s)

        for share in shares:
            t.add_row(share)
        t.add_row(['Total price', '######', '######', str(round(portfolio['cost'], 2))+"$"])
        t.add_row(['Total profit', '######', '######', str(round(portfolio['return'], 2))+"$"])
        t.add_row(['Total recovered', '######', '######', str(round(portfolio['sum'], 2))+"$"])
        print(f"Starting balance : {self.amount}$")
        print(t.get_string(title="AlgoInvest&Trade"))

    def main(self):
        shares = self.serializer(self.filename)
        n = len(shares)
        max_profit = 0
        for size in range(1, n+1):
            combinations = list(self.combinations(shares, size))
            for comb in combinations:
                cost, profit = self.calculate_cost_and_profit(comb)
                if cost < self.amount and profit > max_profit:
                    max_profit = profit
                    portfolio = self.portfolio(comb, cost, profit)
        self.display(portfolio)


if __name__ == '__main__':
    start_time = time.time()
    amount = 500
    filename = 'dataset0'
    bruteforce = BruteForce(amount, filename)
    bruteforce.main()
    print("--- %s seconds ---" % (time.time() - start_time))
