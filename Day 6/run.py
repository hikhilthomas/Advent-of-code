import timeit

def findPath(currRow, currCol, matrix, visited = None, direction = 0, checkLoop = False):
    if visited is None:
        visited = set()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    nextRow = directions[direction][0]
    nextCol = directions[direction][1]
    count = 0

    while 0 <= currRow < len(matrix) and 0 <= currCol < len(matrix[0]):

        if not checkLoop:
            if 1 <= currRow < len(matrix) - 1 and 1 <= currCol < len(matrix[0]) - 1 and matrix[currRow + nextRow][currCol + nextCol] != "#":
                matrix[currRow + nextRow][currCol + nextCol] = "#"

                alreadyVisited = False
                for currDir in [0, 1, 2, 3]:
                    if (currRow + nextRow, currCol + nextCol, currDir) in visited:
                        alreadyVisited = True

                if not alreadyVisited and findPath(currRow, currCol, matrix, set(), direction, True):
                    count += 1
                matrix[currRow + nextRow][currCol + nextCol] = "."
        else:
            if (currRow, currCol, direction) in visited:
                return True

        visited.add((currRow, currCol, direction))

        # If next position is blocked, change direction and go to the start of the loop without moving
        if 0 <= currRow + nextRow < len(matrix) and 0 <= currCol + nextCol < len(matrix[0]) and matrix[currRow + nextRow][currCol + nextCol] == '#':
            direction = (direction + 1) % 4
            nextRow = directions[direction][0]
            nextCol = directions[direction][1]
            continue

        currRow += nextRow
        currCol += nextCol

    if checkLoop:
        return False

    # done to use timeit.timeit()
    return str(count)

def main():
    startRow, startCol, matrix = importTests()
    print(findPath(startRow, startCol, matrix))
    executionTime = timeit.timeit(findPath(startRow, startCol, matrix), number=1000)
    print(f"Execution time: {executionTime:.6f} seconds")


def importTests():
    matrix = []
    startRow, startCol = 0, 0
    with open("tests.txt", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            line = [i for i in lines[i].strip()]
            if '^' in line:
                startRow = i
                startCol = line.index('^')
            matrix.append(line)
    return startRow, startCol, matrix


if __name__ == "__main__":
    main()
