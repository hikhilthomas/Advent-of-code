from TestHelper import generate_file_name


def fetch_input() -> str:
    file_path = generate_file_name(__file__, "test.txt")
    with open(file_path, "r") as f:
        return f.readline().strip()


def calculate_arrangements(stone: str, param: int, memo: dict):
    if stone.startswith("0"):
        stone = str(int(stone))
    if param == 0:
        return 1

    memo_key = f"{stone}-{param}"
    if memo_key in memo:
        return memo[memo_key]

    if stone == "0":
        memo[memo_key] = calculate_arrangements("1", param - 1, memo)
    elif len(stone) % 2 == 0:
        middle = len(stone) // 2
        left_stone = stone[:middle]
        right_stone = stone[middle:]
        memo[memo_key] = (calculate_arrangements(left_stone, param - 1, memo) +
                          calculate_arrangements(right_stone, param - 1, memo))
    else:
        new_stone = int(stone) * 2024
        out = calculate_arrangements(str(new_stone), param - 1, memo)
        memo[memo_key] = out
    return memo[memo_key]


def find_num_of_stones(arrangement: str, ) -> int:
    total_stones = 0
    memo = dict()
    for stone in arrangement.split():
        out = calculate_arrangements(stone, 75, memo)
        total_stones += out
    return total_stones


def main():
    arrangement = fetch_input()
    print(find_num_of_stones(arrangement))


if __name__ == "__main__":
    main()
