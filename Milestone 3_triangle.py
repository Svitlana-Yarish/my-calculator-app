from typing import List


def get_triangle(rows: int) -> List[List[int]]:
    triangle = []

    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
        
    return triangle


num_rows = int(input("Введіть кількість рядків для трикутника: "))
result = get_triangle(num_rows)
for row in result:
    print(row)


for i in range(len(result)):   
    print(' ' * (len(result) - i - 1), end='')
    print(' '.join(map(str, result[i])))

