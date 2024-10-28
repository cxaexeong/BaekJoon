import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, arr):
    v[start] = 1
    team.append(start)
    num = nums[start]
    if v[num]:
        if num in team:
            arr += team[team.index(num):]
        return
    else:
        dfs(num, arr)
        
for _ in range(int(input())):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    v = [0 for _ in range(n+1)]
    # 팀을 이룬 학생
    student = []
    for i in range(1,n+1):
        if not v[i]:
            team = []
            dfs(i, student)
    print(n - len(student))