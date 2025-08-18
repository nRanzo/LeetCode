class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        q = deque() # for rotten oranges

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        if fresh == 0:
            return 0

        time = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        while q and fresh > 0:
            # at this point len(q) = x
            for _ in range(len(q)): # x iterations, even if I modify q inside this loop
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    # if in bounds and fresh becomes rotten
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1