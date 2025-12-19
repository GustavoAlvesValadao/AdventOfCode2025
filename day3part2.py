def new_bigger_joltage(line, k=12):
    digits = list(map(int, line.strip()))
    n = len(digits)

    array = []
    to_remove = n - k

    for d in digits:
        while to_remove > 0 and array and array[-1] < d:
            array.pop()
            to_remove -= 1
        array.append(d)

    array = array[:k]

    return int("".join(map(str, array)))


def total_sum(banks):
    return sum(new_bigger_joltage(line) for line in banks)

banks = [
  "987654321111111",
  "811111111111119",
  "234234234234278",
  "818181911112111",
]

print(total_sum(banks))
