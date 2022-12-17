with open('C:/Users/shrom/Downloads/17(1).txt') as file:
    pairs = 0
    max_sum = 0

    nums = [int(x.replace('\n', '')) for x in file.readlines()]

    seven = max([x for x in nums if x % 7 == 0])

    for i in range(len(nums) - 1):
        a, b = nums[i], nums[i + 1]

        if (a % 7 == 0 or b % 7 == 0) and a + b < seven:
            pairs += 1
            if a + b > max_sum:
                max_sum = a + b

print(pairs, max_sum)
