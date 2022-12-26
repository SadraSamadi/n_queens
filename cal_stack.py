def main():
    next = True
    s=7
    while(next):
        size = s
        print("Size of board: %d" % size) 
        bt = BackTrackTC(size)
        _,next = bt.solve_backtrack()
        s+=1
        print()

class BackTrackTC:

    def __init__(self, size):
        self.size = size    
    def solve_backtrack(self):
        if self.size < 1:
            return []
        solutions = []
        stack = [[]]
        prev_sol_len = 0
        total_stack_len = 0
        while stack:
            solution = stack.pop(0)
            if len(solution) != prev_sol_len:
                print(f"After filling {prev_sol_len+1} row, length of stack is {len(stack)+1}")
                prev_sol_len = len(solution)
                # if prev_sol_len == 5:
                #     for s in stack:
                #         self.print(s)
                total_stack_len += len(stack)+1
            row = len(solution)
            if row == self.size:
                solutions.append(solution)
                continue
            
            for col in range(self.size):
                queen = (row, col)
                queens = solution.copy()
                queens.append(queen)
                if not self.conflict_with_top_row_queen(queens):
                    stack.append(queens)
        print(f"Total stack length: {total_stack_len}")
        if total_stack_len>self.size**3 and total_stack_len<self.size**4:
            return solutions,True
        return solutions,False

    def conflict_with_top_row_queen(self, queens):
        i = len(queens)-1
        for j in range(0, i):
            a, b = queens[i]
            c, d = queens[j]
            if a == c or b == d or abs(a - c) == abs(b - d):
                return True
        return False

    def print(self, queens):
        for i in range(self.size):
            print('-' * self.size)
            for j in range(self.size):
                p = 'Q' if (i, j) in queens else ' '
                print('|%s' % p, end='')
            print('|')
        print('-' * self.size)


if __name__ == '__main__':
    main()
