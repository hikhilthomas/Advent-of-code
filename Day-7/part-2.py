from TestHelper import generate_file_name


def canGenerateResult(currSum, idx, result, equation):
    if idx == len(equation):
        if currSum == result:
            return True
        else:
            return False
    return (canGenerateResult(currSum + equation[idx], idx + 1, result, equation) or
            canGenerateResult(currSum * equation[idx], idx + 1, result, equation) or
            canGenerateResult(int(str(currSum) + str(equation[idx])), idx + 1, result, equation))


def calibrationResult(equations: dict) -> int:
    totalCalibrationResult = 0
    for result, equation in equations.items():
        if canGenerateResult(equation[0], 1, result, equation):
            totalCalibrationResult += result
    return totalCalibrationResult


def findCalibrationResult() -> int:
    equations = dict()

    file_path = generate_file_name(__file__, "test.txt")
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            key = int(line.split(":")[0])
            val = [int(num) for num in line.split(":")[1].strip().split(" ")]
            equations[key] = val
    return calibrationResult(equations)


def main():
    print(findCalibrationResult())


if __name__ == "__main__":
    main()
