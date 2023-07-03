# n: 연산할 수
# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.
# 출력: 위에 3가지 연산을 활용해 n을 1로 만들기위해 최소 연산횟수
import sys

n = int(sys.stdin.readline())
d = [0] * (n + 1)

for i in range(2, n+1):
    d[i] = d[i - 1] + 1 # d = [0, 0, 1, 2, 3....., n-1]
    if i % 3 == 0:
        # 현재수와 3으로 나눈거에 1을 더한숫자중 작은값을 삽입
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 2 == 0:
        # 현재수와 2으로 나눈거에 1을 더한숫자중 작은값을 삽입
        d[i] = min(d[i], d[i // 2] + 1)
    # ex) d =  [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3]
print(d[n])