from TestHelper import generate_file_name


def findAntinode(location: [int, int], pairLocation: [int, int], diff: [int, int],
                 map: [[int, int]], uniqueAntinodes: set):
    possibleLocation1 = [location[0] + diff[0], location[1] + diff[1]]
    possibleLocation2 = [location[0] - diff[0], location[1] - diff[1]]
    antinode = possibleLocation1 if possibleLocation1[0] != pairLocation[0] else possibleLocation2
    if 0 <= antinode[0] < len(map) and 0 <= antinode[1] < len(map[0]):
        uniqueAntinodes.add(str(antinode))


def findUniqueAntinodes(map: [[int, int]], frequencyLocations: dict) -> int:
    uniqueAntinodes = set()
    for locations in frequencyLocations.values():
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                diff = [locations[i][0] - locations[j][0], locations[i][1] - locations[j][1]]
                findAntinode(locations[i], locations[j], diff, map, uniqueAntinodes)
                findAntinode(locations[j], locations[i], diff, map, uniqueAntinodes)
    return len(uniqueAntinodes)


def findUniqueAntinodeLocations() -> int:
    map = []
    frequencyLocations = dict()

    file_path = generate_file_name(__file__, "test.txt")
    with open(file_path, "r") as f:
        lines = f.readlines()

        # Find all the frequency locations
        for i in range(len(lines)):
            row = lines[i].strip()
            col = []
            for j in range(len(row)):
                col.append(row[j])
                if row[j] != ".":
                    frequency = row[j]
                    if frequency not in frequencyLocations:
                        frequencyLocations[frequency] = []
                    frequencyLocations[frequency].append([i, j])
            map.append(col)

    return findUniqueAntinodes(map, frequencyLocations)


def main():
    print(findUniqueAntinodeLocations())


if __name__ == "__main__":
    main()
