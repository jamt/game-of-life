import sys

__author__ = 'James Thomas'


def neighbors(grid, i, j):
    count = 0
    for x in xrange(i - 1, i + 2):
        for y in xrange(j - 1, j + 2):
            if (x != i or y != j) and (x >= 0 and y >= 0):
                try:
                    if grid[x][y] == 1:
                        count += 1
                except IndexError:
                    pass
    return count


def rules(grid, new_grid, i, j):
    live = neighbors(grid, i, j)
    if grid[i][j] == 1 and (live < 2 or live > 3):
            new_grid[i][j] = 0
    if grid[i][j] == 0 and live == 3:
        new_grid[i][j] = 1


def main(infile, games):
    with open(infile, "rb") as file:
        grid = [[int(x) for x in list(line.strip())] for line in file]
    for x in xrange(games):
        new_grid = [list(row) for row in grid]
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
               rules(grid, new_grid, i, j)
        print "Result of game number " + str(x+1)
        for row in xrange(len(new_grid)):
            print ''.join(map(str, new_grid[row]))
        grid = new_grid


if __name__ == "__main__":
    infile = sys.argv[1]
    games = int(sys.argv[2])
    main(infile, games)
