def count_zeros_method_0x434C49434B(rotations):
    pos = 50
    zeros = 0

    for rot in rotations:
        direction = rot[0].upper()
        steps = int(rot[1:])

        if direction == 'R':
            first = (100 - pos) % 100
        else:
            first = pos % 100

        if first == 0:
            first = 100

        if first <= steps:
            zeros += 1 + (steps - first) // 100

        if direction == 'R':
            pos = (pos + steps) % 100
        else:
            pos = (pos - steps) % 100

    return zeros

rotations = [
        "L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"
]

print(count_zeros_method_0x434C49434B(rotations))
