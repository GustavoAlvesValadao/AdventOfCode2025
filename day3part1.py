def bigger_joltage(line):
    digits = list(map(int, line.strip()))
    bigger = -1

    for i in range(len(digits) - 1):
        for j in range(i + 1, len(digits)):
            value = digits[i] * 10 + digits[j]
            if value > bigger:
                bigger = value

    return bigger


def total_sum(banks):
    return sum(bigger_joltage(line) for line in banks)

banks = [
"987654321111111",
"811111111111119",
"234234234234278",
"818181911112111",
]

print(total_sum(banks))
