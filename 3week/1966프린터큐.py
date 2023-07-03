import sys

test_cases = int(sys.stdin.readline())

for _ in range(test_cases):
    n, m = list(map(int, sys.stdin.readline().split()))
    imp = list(map(int, sys.stdin.readline().split()))
    idx = list(range(len(imp)))
    idx[m] = 'target'

    # 순서
    order = 0

    while True:
        if imp[0] == max(imp):
            order += 1

            if idx[0] == 'target':
                print(order)
                break
            else:
                imp.pop(0)
                idx.pop(0)

        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))

#  몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M 이 무엇을 말하는건지 잘 이해가 가지않음