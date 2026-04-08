import ast

def solve_flood_fill():
    try:
        with open('input.txt', 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]

        if not lines:
            print("Файл input.txt порожній.")
            return

        height, width = map(int, lines[0].split(','))
        
        start_r, start_c = map(int, lines[1].split(','))
        
        replace_color = lines[2].replace("'", "").replace('"', "").replace("‘", "").replace("’", "")
        
        matrix = []
        for line in lines[3:]:
            clean_line = line.rstrip(',')
            clean_line = clean_line.replace("‘", "'").replace("’", "'")
            
            row = ast.literal_eval(clean_line)
            matrix.append(row)

        target_color = matrix[start_r][start_c]

        if target_color != replace_color:
            queue = [(start_r, start_c)]
            matrix[start_r][start_c] = replace_color
            
            while queue:
                r, c = queue.pop(0)
                
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < height and 0 <= nc < width:
                        if matrix[nr][nc] == target_color:
                            matrix[nr][nc] = replace_color
                            queue.append((nr, nc))

        with open('output.txt', 'w', encoding='utf-8') as f:
            for row in matrix:
                formatted_row = "[" + ", ".join([f"'{val}'" for val in row]) + "]\n"
                f.write(formatted_row)
                
        print("Заливку успішно завершено! Результат збережено у файл output.txt.")

    except FileNotFoundError:
        print("Помилка: Файл input.txt не знайдено.")
    except Exception as e:
        print(f"Сталася помилка при обробці даних: {e}")

if __name__ == "__main__":
    solve_flood_fill()