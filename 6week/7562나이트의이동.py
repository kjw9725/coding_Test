# t: 테스트케이스의 수
# l: 한변의 길이
# 나이트의 현재칸
# 나이트가 이동할 칸
from collections import deque
import sys
sys.setrecursionlimit(10**9)

t = int(sys.stdin.readline())
direction = [[2, 1], [-2, 1], [2, -1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

def bfs():


for _ in range(t):
    l = int(sys.stdin.readline())
    graph = [[0]*l for _ in range(l)]
    x1, y1 = map(int, sys.stdin.readline().split())
    x2, y2 = map(int, sys.stdin.readline().split())
    bfs(x1, y1)
