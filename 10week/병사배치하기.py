# n: 병사의 수
# 병사들의 전투력
# 전투력이 높은것부터 내림차순으로 배치되도록 병사를 열외시킨다 병사의 수가 최대가 되게 열외해야하는 병사의수
# 출력: 전투력이 내림차순으로 정렬되고 병사의 수가 최대가 되게 열외해야하는 병사의수
import sys

n = int(sys.stdin.readline())
soldier = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in range(n):
    if i > 0 and i < n-1 and soldier[i] < soldier[i-1] and soldier[i] < soldier[i+1]:
        cnt += 1
        soldier[i] = soldier[i-1]
    # elif i == 0 and soldier[i] > soldier[n-1]:
    #     cnt += 1
print(cnt)