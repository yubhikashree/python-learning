def sum_above(numbers, threshold):
    total = 0
    for num in numbers:
        if num > threshold:
            total += num
    return total
nums = [10, 25, 8, 42, 15, 33]
print(sum_above(nums, 20))