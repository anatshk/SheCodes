def middle_way(a, b):
    return [a[1], b[1]]


def string_match(a, b):
    total = 0
    for i in range(len(a)-1):
        if i >= len(b)-1:
            break
        substr_a = a[i:i+2]
        substr_b = b[i:i+2]
        if substr_a == substr_b:
            total += 1
    return total

# string_match('xxcaazz', 'xxbaaz')


def same_first_last(nums):
    if len(nums) >= 1 and nums[0] == nums[-1]:
        return True
    return False