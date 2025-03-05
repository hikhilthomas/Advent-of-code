from TestHelper import generate_file_name


def calculate_checksum(disk_map: list) -> int:
    check_sum = 0
    for i in range(len(disk_map)):
        if disk_map[i] == '.':
            continue
        check_sum += disk_map[i] * i

    return check_sum


def find_size(disk_map: list, idx: int, is_file: bool) -> int:
    if idx < 0 or idx >= len(disk_map):
        return 0
    count = 1
    if is_file:
        while idx >= 0 and disk_map[idx] == disk_map[idx - 1]:
            count += 1
            idx -= 1
    else:
        while idx < len(disk_map) and disk_map[idx] == '.':
            count += 1
            idx += 1
    return count


def generate_checksum(expanded_disk_map: list) -> int:
    right_idx = len(expanded_disk_map) - 1
    left_idx = 0
    updated = set()
    while right_idx >= 0 and left_idx < len(expanded_disk_map):
        while (expanded_disk_map[right_idx] == '.') or right_idx in updated:
            right_idx -= 1
        right_size = find_size(expanded_disk_map, right_idx, True)
        if not right_size:
            break
        num = expanded_disk_map[right_idx]

        left_size = 0
        while left_size < right_size:
            left_idx += left_size
            while (left_idx < right_idx and expanded_disk_map[left_idx] != '.') or left_idx in updated:
                left_idx += 1
            left_size = find_size(expanded_disk_map, left_idx, False) - 1
            if not left_size:
                break

        if right_size <= left_size:
            temp = right_size
            while temp > 0:
                expanded_disk_map[left_idx + temp - 1] = num
                updated.add(left_idx + temp - 1)
                expanded_disk_map[right_idx - temp + 1] = "."
                temp -= 1

        right_idx = right_idx - right_size
        left_idx = 0

    return calculate_checksum(expanded_disk_map)


def expand_disk_and_generate_checksum(disk_map: list) -> int:
    expanded_disk_map = []

    is_free_space = False
    num = 0
    for i in range(len(disk_map)):
        disk_id = "." if is_free_space else num
        for j in range(disk_map[i]):
            expanded_disk_map.append(disk_id)
        is_free_space = True if not is_free_space else False
        num = num + 1 if num == disk_id else num

    return generate_checksum(expanded_disk_map)


def find_checksum() -> int:
    file_path = generate_file_name(__file__, "test.txt")
    with open(file_path, "r") as f:
        line = f.readline()
        disk_map = [int(i) for i in line]

    return expand_disk_and_generate_checksum(disk_map)


def main():
    print(find_checksum())


if __name__ == "__main__":
    main()
