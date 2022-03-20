#!/usr/bin/python3

# import csv

# with open('input_sample.csv') as read_obj:
#     csv_reader = csv.reader(read_obj)
#     rows = list(csv_reader)
portfolio = {}
# for row in rows:
#     row = [int(row[0]),row[1],int(row[2]),int(row[3])]
#     if row[1] not in portfolio.keys():
#         portfolio[row[1]] = [row]
#     else:
#         portfolio[row[1]].append(row)

# with open('input_sample.csv') as f:
import sys
with open(sys.argv[1]) as f:
    rows = f.readlines()
for row in rows:
    row = row.split(',')
    row = [int(row[0]),row[1],int(row[2]),int(row[3])]
    if row[1] not in portfolio.keys():
        portfolio[row[1]] = [row]
    else:
        portfolio[row[1]].append(row)

def maxTimeGap(allTransactions):
    allTransactions = sorted(allTransactions, key = lambda x: x[0]) # make sure it is sorted by time stamp
    max_gap = 0
    if len(allTransactions) == 1:
        return max_gap
    else:
        for i, transaction in enumerate(allTransactions[1:]):
            gap = transaction[0] - allTransactions[i][0]
            if gap > max_gap:
                max_gap = gap
    return max_gap

def volume(allTransactions):
    result = sum (x[2] for x in allTransactions)
    return result

def weigtedAveragePrice(allTransactions):
    total_price = sum (x[2] * x[3] for x in allTransactions)
    total_volume = volume(allTransactions)
    return int(total_price/total_volume)

def maxPrice(allTransactions):
    result = max(x[3] for x in allTransactions)
    return result


shares = list(portfolio.keys())
shares.sort()
for share in shares:
    MaxTimeGap = maxTimeGap(portfolio[share])
    Volume = volume(portfolio[share])
    WeigtedAveragePrice = weigtedAveragePrice(portfolio[share])
    MaxPrice = maxPrice(portfolio[share])
    print(f'{share},{MaxTimeGap},{Volume},{WeigtedAveragePrice},{MaxPrice}')