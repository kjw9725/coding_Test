import sys

n = int(sys.stdin.readline())
time = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    time.append([a,b])

time.sort(key=lambda a: a[0])
time.sort(key=lambda a: a[1])
