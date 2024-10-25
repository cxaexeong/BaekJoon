from collections import deque

# 이동 가능한 여섯 가지 방향 (위, 아래, 앞, 뒤, 왼쪽, 오른쪽)
dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]

def bfs(l, r, c, start, end, building):
    q = deque([start])
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]
    visited[start[0]][start[1]][start[2]] = True
    time = [[[0] * c for _ in range(r)] for _ in range(l)]

    while q:
        z, x, y = q.popleft()

        # 탈출구에 도달한 경우
        if (z, x, y) == end:
            return time[z][x][y]

        # 여섯 방향으로 이동
        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            
            # 범위를 벗어나지 않고, 벽('#')이 아니며, 방문하지 않은 경우
            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c:
                if not visited[nz][nx][ny] and building[nz][nx][ny] != '#':
                    visited[nz][nx][ny] = True
                    time[nz][nx][ny] = time[z][x][y] + 1
                    q.append((nz, nx, ny))

    # 탈출구에 도달하지 못한 경우
    return "Trapped!"

while True:
    # 입력 처리
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break

    building = []
    start = end = None

    # 빌딩의 각 층 입력
    for i in range(l):
        floor = []
        for j in range(r):
            line = list(input().strip())
            floor.append(line)
            for k in range(c):
                if line[k] == 'S':
                    start = (i, j, k)
                elif line[k] == 'E':
                    end = (i, j, k)
        building.append(floor)
        input()  # 빈 줄 처리

    # BFS 탐색
    result = bfs(l, r, c, start, end, building)
    if result == "Trapped!":
        print("Trapped!")
    else:
        print(f"Escaped in {result} minute(s).")
