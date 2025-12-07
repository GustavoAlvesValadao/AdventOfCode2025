def is_repetition(n: int) -> bool:
    s = str(n)
    L = len(s)

    for bloc_len in range(1, L // 2 + 1):
        if L % bloc_len != 0:
            continue

        bloc = s[:bloc_len]
        repetitions = L // bloc_len

        if bloc * repetitions == s and repetitions >= 2:
            return True

    return False


def find_repetitions(intervals_str: str):
    invalids = []
    intervals = intervals_str.split(",")

    for interval in intervals:
        if not interval.strip():
            continue

        start, end = interval.split("-")
        start, end = int(start), int(end)

        for n in range(start, end + 1):
            if is_repetition(n):
                invalids.append(n)

    return invalids

intervals_example = (
    "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
    "1698522-1698528,446443-446449,38593856-38593862,565653-565659,"
    "824824821-824824827,2121212118-2121212124"
)

invalids = find_repetitions(intervals_example)

print("Quantidade de inválidos:", len(invalids))
print("Soma total:", sum(invalids))
