import time
from n_queens import NQueens


def main():
    # print('.: N-Queens Problem :.')
    # size = int(input('Please enter the size of board: '))
    for s in range(6,8):
        size = s
        # print_solutions = input('Do you want the solutions to be printed (Y/N): ').lower() == 'y'
        print_solutions = False
        n_queens = NQueens(size)
        # calcuate time taken execution of the function
        
        time_start = time.time()
        dfs_solutions = n_queens.solve_dfs()
        time_end = time.time()
        total_dfs_time = time_end - time_start
        time_start = time.time()
        bfs_solutions = n_queens.solve_bfs()
        time_end = time.time()
        total_bfs_time = time_end - time_start
        time_start = time.time()
        backtrack_solutions = n_queens.solve_backtrack()
        time_end = time.time()
        total_backtrack_time = time_end - time_start
        
        if print_solutions:
            for i, solution in enumerate(dfs_solutions):
                print('DFS Solution %d:' % (i + 1))
                n_queens.print(solution)
            for i, solution in enumerate(bfs_solutions):
                print('BFS Solution %d:' % (i + 1))
                n_queens.print(solution)
            for i, solution in enumerate(backtrack_solutions):
                print('Backtrack Solution %d:' % (i + 1))
                n_queens.print(solution)
        print("Size of board: %d" % size)   
        print('Total time taken for DFS solutions:       %f' % total_dfs_time)
        print('Total time taken for BFS solutions:       %f' % total_bfs_time)
        print('Total time taken for Backtrack solutions: %f' % total_backtrack_time)
        print()


if __name__ == '__main__':
    main()
