from TestHelper import generate_file_name


def fetch_input() -> str:
    file_path = generate_file_name(__file__, "test.txt")
    with open(file_path, "r") as f:
        return f.readline().strip()


def calculate_arrangements(stone: str, param: int):
    if stone.startswith("0"):
        stone = str(int(stone))
    if param == 0:
        return 1
    if stone == "0":
        return calculate_arrangements("1", param - 1)
    elif len(stone) % 2 == 0:
        middle = len(stone) // 2
        left_stone = stone[:middle]
        right_stone = stone[middle:]
        return (calculate_arrangements(left_stone, param - 1) +
                calculate_arrangements(right_stone, param - 1))
    else:
        new_stone = int(stone) * 2024
        return calculate_arrangements(str(new_stone), param - 1)


def find_num_of_stones(arrangement: str) -> int:
    total_stones = 0
    for stone in arrangement.split():
        total_stones += calculate_arrangements(stone, 25)
    return total_stones


def main():
    arrangement = fetch_input()
    print(find_num_of_stones(arrangement))


if __name__ == "__main__":
    main()
