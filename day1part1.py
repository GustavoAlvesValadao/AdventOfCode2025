def count_zeros(rotations):
    pos = 50
    zeros = 0

    for rot in rotations:
        direction = rot[0]
        value = int(rot[1:])

        if direction == 'L':
            pos = (pos - value) % 100
        else: 
            pos = (pos + value) % 100

        if pos == 0:
            zeros += 1

    return zeros

rotations = [
    "L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"
    ]

print(count_zeros(rotations))
