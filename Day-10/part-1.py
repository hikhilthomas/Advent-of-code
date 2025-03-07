from TestHelper import generate_file_name


def generate_map() -> (list, list):
    topographic_map = []
    file_path = generate_file_name(__file__, "test.txt")
    trails = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            _ = []
            for j in range(len(lines[i].strip())):
                height = int(lines[i][j])
                if height == 0:
                    trails.append([i, j])
                _.append(height)
            topographic_map.append(_)
    return topographic_map, trails


def calculate_trailhead_sums(row: int, col: int, topographic_map: list, prev: int, visited: set) -> int:
    prev += 1
    if (row < 0 or row >= len(topographic_map)
            or col < 0 or col >= len(topographic_map[0])
            or (row, col) in visited
            or topographic_map[row][col] != prev):
        return 0
    elif topographic_map[row][col] == 9:
        visited.add((row, col))
        return 1
    return (calculate_trailhead_sums(row - 1, col, topographic_map, prev, visited)
            + calculate_trailhead_sums(row + 1, col, topographic_map, prev, visited)
            + calculate_trailhead_sums(row, col - 1, topographic_map, prev, visited)
            + calculate_trailhead_sums(row, col + 1, topographic_map, prev, visited))


def calculate_trailhead_scores(topographic_map: list, trail_heads: list) -> list:
    scores = []
    for i in range(len(trail_heads)):
        row, col = trail_heads[i]
        visited = set()
        scores.append(calculate_trailhead_sums(row, col, topographic_map, -1, visited))
    return scores


def calculate_trailhead_sum() -> int:
    topographic_map, trail_heads = generate_map()
    scores = calculate_trailhead_scores(topographic_map, trail_heads)
    return sum(scores)


def main():
    print(calculate_trailhead_sum())


if __name__ == "__main__":
    main()
