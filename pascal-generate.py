def generatePascal(height):
    if height <= 0:
        return []

    rows = [[1]]
    for i in range(1, height):
        prev_row = rows[i-1]
        curr_row = [1]
        for j in range(1, i):
            curr_row.append(prev_row[j-1] + prev_row[j])
        curr_row.append(1)
        rows.append(curr_row)
    return rows

triangle = generatePascal(5)
for row in triangle:
    print(row)