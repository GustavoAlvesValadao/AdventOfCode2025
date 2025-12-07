def double_repetition(n: int) -> bool:
    s = str(n)
    if len(s) % 2 != 0:
        return False

    half = len(s) // 2
    return s[:half] == s[half:]


def find_invalid(intervals_str: str):
    invalids = []
    intervals = intervals_str.split(",")

    for interval in intervals:
        if not interval.strip():
            continue

        start, end = interval.split("-")
        start, end = int(start), int(end)

        for n in range(start, end + 1):
            if double_repetition(n):
                invalids.append(n)

    return invalids

intervals_example = (
"11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
"1698522-1698528,446443-446449,38593856-38593862,565653-565659,"
"824824821-824824827,2121212118-2121212124"
)

invalids = find_invalid(intervals_example)

print("IDs inválidos encontrados:", len(invalids))
print(invalids)
print("\nSoma total:", sum(invalids))
