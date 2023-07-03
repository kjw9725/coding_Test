import sys

a, b = map(int, sys.stdin.readline().split())
c, d, e = map(int, sys.stdin.readline().split())
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]  #북 동 남 서
map_list = []
count = 0

for _ in range(b):
    map_list.append(list(map(int, sys.stdin.readline().split())))

while True:
    for i in direction:
        if map_list[a + i[c]][b + i[d]] == 0:
            count += 1