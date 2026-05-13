def count_paths(w: int, h: int, grid: list[str]) -> int:
    if w == 0 or h == 0:
        return 0
        
    sum_char = {chr(97 + i): 0 for i in range(26)}
    
    prev_dp = [1] * h
    curr_dp = [0] * h
    
    for i in range(h):
        sum_char[grid[i][0]] += 1
        
    for j in range(1, w):
        for i in range(h):
            ch = grid[i][j]
            ways = sum_char[ch]
            
            if grid[i][j-1] != ch:
                ways += prev_dp[i]
                
            curr_dp[i] = ways
            
        for i in range(h):
            sum_char[grid[i][j]] += curr_dp[i]
            
        prev_dp, curr_dp = curr_dp, prev_dp
        
    if h == 1:
        return prev_dp[0]
    else:
        return prev_dp[0] + prev_dp[h-1]


def solve_file(input_filename: str = "ijones.in", output_filename: str = "ijones.out"):
    with open(input_filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
        
    w, h = map(int, lines[0].split())
    grid = lines[1:h+1]
    
    result = count_paths(w, h, grid)
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(str(result) + '\n')


if __name__ == "__main__":
    solve_file()