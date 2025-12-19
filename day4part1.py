def count_movable_rolls(grid):
    rows = len(grid)
    cols = len(grid[0])

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),         ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

    def neighbors_count(r, c):
        count = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == '@':
                    count += 1
        return count

    movable = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                if neighbors_count(r, c) < 4:
                    movable += 1

    return movable

input = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".strip()

grid = input.split("\n")

print(count_movable_rolls(grid))
