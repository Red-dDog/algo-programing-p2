def build_transition_table(needle: str) -> list[dict]:
    m = len(needle)
    alphabet = set(needle)
    tf = [{} for _ in range(m + 1)]
    
    for q in range(m + 1):
        for char in alphabet:
            k = min(m, q + 1)
            s = needle[:q] + char
            while k > 0 and not s.endswith(needle[:k]):
                k -= 1
            tf[q][char] = k
            
    return tf

def search_fsa(haystack: str, needle: str) -> list[int]:
    if not needle:
        return []
        
    m = len(needle)
    tf = build_transition_table(needle)
    state = 0
    indices = []
    
    for i, char in enumerate(haystack):
        state = tf[state].get(char, 0)
        if state == m:
            indices.append(i - m + 1)
            
    return indices

if __name__ == "__main__":
    text = "AABAACAADAABAABA"
    pattern = "AABA"
    result = search_fsa(text, pattern)
    print(f"Індекси входжень '{pattern}' у текст: {result}")