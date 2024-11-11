class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        def dfs(i, r, c):
            if i == len(word):
                return True
            char = board[r][c]
            if char != word[i]:
                return False
            board[r][c] = '#'
            for nei_r, nei_c in (r+1,c), (r-1,c), (r,c+1), (r,c-1):
                if R > nei_r >= 0 <= nei_c < C:
                    if board[nei_r][nei_c] == '#':
                        continue        
                    if dfs(i+1, nei_r, nei_c):
                        return True        
            board[r][c] = char
            return False
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0] and dfs(0, r, c):                    
                    return True
        return False
        