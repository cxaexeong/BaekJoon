import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(start, arr):
    visited[start] = 1
    cycle.append(start)
    num = nums[start]
    if visited[num]:
        if num in cycle:
            arr += cycle[cycle.index(num):]
        return
    else:
        dfs(num, arr)

for _ in range(int(input())):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    visited = [0 for _ in range(n + 1)]
    # 팀을 이룬 학생
    student = []
    for now in range(1, n + 1):
        if not visited[now]:
            cycle = []
            dfs(now, student)
    print(n - len(student))