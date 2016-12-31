def reverse(lst):
    if not lst: return []
    return [lst[-1]] + reverse(lst[:-1])

print(reverse([1,2,3,4,5]))