#import order: from module import method
from collections import deque 

def numIslands(grid):
    #in the event of no grid return 0
    if not grid:
        return 0
    
    #bfs
    def bfs(r,c):
        #initalize the queue that will hold the nearby cells to search
        search_queue = deque()
        #add current cell to queue and visited
        visited.add((r,c))
        search_queue.append((r,c))

        #iterate through the cells needed to be processed
        while search_queue:
            #set movement patterns to capture the nearby cells
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            #pop current cell
            row,col = search_queue.popleft()
            
            #iterate through each direction (segmenet in which I forget)
            for dr, dc in directions:
                r,c = row+dr, col+dc
                if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited):
                    #add current cell to queue and visited
                    search_queue.append((r,c))
                    visited.add((r,c))

    
    #initialize 4 var (count, rows, cols, visited)
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    #traverse the matrix
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visited:
                bfs(r,c) #why using bfs?
                count += 1
    return count

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(numIslands(grid))

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid))