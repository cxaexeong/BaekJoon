from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque([(0, 0, 0)])  # (x, y, 벽 부순 여부)
    v[0][0][0] = 1  # 시작점은 거리 1로 설정

    while q:
        x, y, broken = q.popleft()

        # 도착점에 도달한 경우
        if x == n - 1 and y == m - 1:
            return v[x][y][broken]

        # 네 방향으로 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 맵 범위 내에서만 이동
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 아니고, 방문하지 않은 경우
                if arr[nx][ny] == 0 and v[nx][ny][broken] == 0:
                    v[nx][ny][broken] = v[x][y][broken] + 1
                    q.append((nx, ny, broken))
                # 벽이고, 아직 벽을 부수지 않은 경우
                if arr[nx][ny] == 1 and broken == 0 and v[nx][ny][1] == 0:
                    v[nx][ny][1] = v[x][y][broken] + 1
                    q.append((nx, ny, 1))

    # 도착점에 도달할 수 없는 경우
    return -1

# 입력 처리
n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
# index 0층: 벽을 안 부수고 가는 경로, 1층: 벽을 부수고 가는 경로
v = [[[0,0] for _ in range(m)] for _ in range(n)]  # 3차원 방문 배열

# BFS 수행 및 결과 출력
result = bfs()
print(result)
