num_test_cases = int(input())

for _ in range(num_test_cases):
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    
    left = 0
    count = 0
    prev = -1
    for right in range(len(numbers)):
        if right == 0:
            prev = numbers[right]
            continue
        if numbers[right] * 2 > prev:
            if right - left >= k:
                count += 1
        else:
            left = right
        prev = numbers[right]
        
    print(count)
            
    
    
    
# testCount = int(input())
# for _ in range(testCount):
#     n,k = input().split()
#     n = int(n)
#     k = int(k)
#     nums = [int(x) for x in input().split()]
#     start = 0
#     count = 0
#     for ind in range(len(nums)):
#         if ind == 0:
#             prev = nums[ind]
#             continue
#         if nums[ind] * 2 > prev:
#             if ind - start>=k:
#                 count += 1
#         else:
#             start = ind
#         prev = nums[ind]
#     print(count)