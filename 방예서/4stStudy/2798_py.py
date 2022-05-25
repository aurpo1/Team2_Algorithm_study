# 백준 2798 블랙잭 python

import sys
input = sys.stdin.readline


n, m = map(int, input().split())
cards = list(map(int, input().split()))

temp = 0
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            temp = cards[i] + cards[j] + cards[k]
            if (temp <= m and temp > result):
                result = temp

print(result)
