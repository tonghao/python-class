import os
import pprint
##
#   将文件love.txt中字符读入到grid中
#  grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]
#
# 将grid打印到屏幕

def grid_from_file(filename,grid):
    f = open(filename)
    for line in f:
        item =[]
        line = line.strip("\n")
        for c in line:
            item.append(c)
        grid.append(item)


def print_grid_pic(grid):
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            print(grid[j][i],end="")
        print()

        # for j in grid[i]:
        #     print(grid[i][j],end="")
        # print()

def main():
    filename = "love.txt"
    path = os.path.dirname(os.path.abspath(__file__))
    # print(path)
    filename = os.path.join(path,"love.txt")
    grid = []
    grid_from_file(filename,grid)
    pprint.pprint(grid)
    print("out:")
    print_grid_pic(grid)

if __name__ == "__main__":
    main()


