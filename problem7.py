def dfs(x, y, N, M, grid, visited):
    # Directions for moving in the grid: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(x, y)]
    visited[x][y] = True
    
    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))

def solve(N, M, G):
    # Find the maximum and minimum heights in the grid
    min_height = min(min(row) for row in G)
    max_height = max(max(row) for row in G)
    
    max_islands = 0
    
    # Try each possible height h
    for h in range(min_height, max_height + 1):
        # Create a grid where each cell is True if its height >= h, else False
        grid = [[1 if G[i][j] >= h else 0 for j in range(M)] for i in range(N)]
        
        # Create a visited array to track visited cells
        visited = [[False] * M for _ in range(N)]
        
        # Count the number of islands for this threshold h
        island_count = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1 and not visited[i][j]:
                    dfs(i, j, N, M, grid, visited)
                    island_count += 1
        
        # Track the maximum number of islands across all thresholds
        max_islands = max(max_islands, island_count)
    
    return max_islands

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        G = [list(map(int, input().split())) for _ in range(N)]
        print(solve(N, M, G))

if __name__ == '__main__':
    main()
