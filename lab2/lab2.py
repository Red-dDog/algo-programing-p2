def merge_sort(arr: list[int]) -> None:
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def hamster_calc(S: int, C: int, hamsters: list[list[int]]):

    if not hamsters or not hamsters[0]:
        return 0

    if S > 109 or S < 0:
        raise ValueError("Значення запасу їжі поза межами")
    if C > 105 or C < 1:
        raise ValueError("Значення кількості хомяків поза межами")
    def can_feed(k):
        if k == 0:
            return True
        costs = [h[0] + h[1] * (k - 1) for h in hamsters]
        merge_sort(costs)

        return sum(costs[:k]) <= S
    low = 0
    high = C
    best_count = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        if can_feed(mid):
            best_count = mid
            low = mid + 1  
        else:
            high = mid - 1
            
    return best_count
