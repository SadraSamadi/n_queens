from itertools import count
from queue import Queue


class NQueens:

    def __init__(self, size):
        self.size = size

    def solve_dfs(self):
        if self.size < 1:
            return []
        solutions = []
        stack = [[]]
        counter = 0
        sol_counter = 0
        while stack:
            counter+=1
            solution = stack.pop()
            row = len(solution)
            if row == self.size:
                sol_counter+=1
                if not self.conflict(solution):
                    solutions.append(solution)
                continue
            if row < self.size:
                for col in range(self.size):
                    queen = (row, col)
                    queens = solution.copy()
                    queens.append(queen)
                    stack.append(queens)
        print(f"DFS: {counter}")
        print(f"Sol_DFS: {sol_counter}")
        return solutions

    def solve_bfs(self):
        if self.size < 1:
            return []
        solutions = []
        queue = Queue()
        queue.put([])
        counter = 0
        sol_counter = 0
        while not queue.empty():
            counter+=1
            solution = queue.get()
            row = len(solution)
            
            if row == self.size:
                sol_counter+=1
                if not self.conflict(solution):
                    solutions.append(solution)
                continue
            if row < self.size:
                for col in range(self.size):
                    queen = (row, col)
                    queens = solution.copy()
                    queens.append(queen)
                    queue.put(queens)       
        print(f"BFS: {counter}")
        print(f"Sol_BFS: {sol_counter}")
        return solutions

    def solve_backtrack(self):
        if self.size < 1:
            return []
        solutions = []
        stack = [[]]
        counter = 0
        sol_counter = 0
        while stack:
            counter+=1
            solution = stack.pop()
            if self.conflict_with_top_row_queen(solution):
                continue
            row = len(solution)
            if row == self.size:
                sol_counter+=1
                if not self.conflict(solution):
                    solutions.append(solution)
                continue
            
            for col in range(self.size):
                queen = (row, col)
                queens = solution.copy()
                queens.append(queen)
                stack.append(queens)
        print(f"Bac: {counter}")
        print(f"Sol_Bac: {sol_counter}")
        return solutions

    def conflict_with_top_row_queen(self, queens):
        i = len(queens)-1
        for j in range(0, i):
            a, b = queens[i]
            c, d = queens[j]
            if a == c or b == d or abs(a - c) == abs(b - d):
                return True
        return False

    def conflict(self, queens):
        for i in range(1, len(queens)):
            for j in range(0, i):
                a, b = queens[i]
                c, d = queens[j]
                if a == c or b == d or abs(a - c) == abs(b - d):
                    return True
        return False
    

    def print(self, queens):
        for i in range(self.size):
            print(' ---' * self.size)
            for j in range(self.size):
                p = 'Q' if (i, j) in queens else ' '
                print('| %s ' % p, end='')
            print('|')
        print(' ---' * self.size)
