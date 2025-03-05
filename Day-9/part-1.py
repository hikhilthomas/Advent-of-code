from TestHelper import generate_file_name


def generate_checksum(expanded_disk_map):
    file_id = 0
    checksum = 0
    left_idx, right_idx = 0, len(expanded_disk_map) - 1
    while left_idx < right_idx:
        if expanded_disk_map[right_idx] == ".":
            right_idx -= 1
            continue

        if expanded_disk_map[left_idx] != ".":
            checksum += expanded_disk_map[left_idx] * file_id
            left_idx += 1
        elif expanded_disk_map[right_idx] != ".":
            checksum += expanded_disk_map[right_idx] * file_id
            right_idx -= 1
            left_idx += 1
        file_id += 1
    if left_idx == right_idx:
        checksum += expanded_disk_map[left_idx] * file_id
    return checksum


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
