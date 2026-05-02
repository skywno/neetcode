from typing import List

class Solution:
    
    # Runtime: 29ms (Beats 37.82%) and Memory 7.7MB (Beats 99.86%)
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[-1 for _ in range(n)] for _ in range(m)]
        def dfs(x: int, y: int) -> int:
            # where x is used for row, y is used for column.
            # exception cases:
            if x == m - 1 and y == n - 1:
                return 0
            elif x == m - 1:
                return 1
            elif y == n - 1:
                return 1
            else:
                if cache[x][y] == -1:
                    res = dfs(x+1, y) + dfs(x, y + 1)
                    cache[x][y] = res
                return cache[x][y]  
        if m == n and m == 1: 
            return 1
        return dfs(0,0)

    # Runtime: 42ms (Beats 11.99%) and Memory 7.7MB (Beats 99.86%)
    def uniquePaths2(self, m: int, n: int) -> int:
        cache = [[-1 for _ in range(n)] for _ in range(m)]
        def dfs(x: int, y: int) -> int:
            # where x is used for row, y is used for column.
            # exception cases:
            if x == m - 1 and y == n - 1:
                return 1
            elif x == m - 1:
                return 1
            elif y == n - 1:
                return 1
            else:
                if cache[x][y] == -1:
                    res = dfs(x+1, y) + dfs(x, y + 1)
                    cache[x][y] = res
                return cache[x][y]  
        return dfs(0,0)

    # Runtime: 28ms (Beats 56.59%) and Memory 7.7MB (Beats 99.86%)
    def uniquePaths3(self, m: int, n: int) -> int:
        cache = [[-1 for _ in range(n)] for _ in range(m)]
        def dfs(x: int, y: int) -> int:
            # where x is used for row, y is used for column.
            # exception cases:
            if x == m - 1 and y == n - 1:
                return 1
            if x >= m or y >= n:
                return 0
            else:
                if cache[x][y] == -1:
                    res = dfs(x+1, y) + dfs(x, y + 1)
                    cache[x][y] = res
                return cache[x][y]  
        return dfs(0,0)