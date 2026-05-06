import csv
import os

def read_matrix_from_csv(file_path: str) -> list[list[int]]:
    
    matrix = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                matrix.append([int(x.strip()) for x in row])
    return matrix

def find_minimum_cable_length(matrix: list[list[int]]) -> int:

    if not matrix:
        return 0
    
    n = len(matrix)
    if n <= 1:
        return 0

    selected = [False] * n
    selected[0] = True
    
    num_edges = 0
    min_cost = 0

    while num_edges < n - 1:
        minimum = float('inf')
        x = 0
        y = 0
        
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and matrix[i][j] > 0:
                        if minimum > matrix[i][j]:
                            minimum = matrix[i][j]
                            x = i
                            y = j
                            
        if minimum == float('inf'):
            raise ValueError("Граф незв'язний, неможливо з'єднати всі острови.")
            
        min_cost += minimum
        selected[y] = True
        num_edges += 1

    return min_cost

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_dir, 'islands.csv')
    
    try:
        matrix = read_matrix_from_csv(csv_file_path)
        min_length = find_minimum_cable_length(matrix)
        print(f"Мінімальна довжина: {min_length}")
    except FileNotFoundError:
        print(f"Помилка: Файл {csv_file_path} не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")