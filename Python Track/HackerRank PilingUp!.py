# Enter your code here. Read input from STDIN. Print output to STDOUT

def myFunction(sideLengths):
    curr_cube_length = float("inf")
    left_runner = 0
    right_runner = len(sideLengths) - 1

    while left_runner <= right_runner: # O(n)
        left_val  = sideLengths[left_runner]
        right_val = sideLengths[right_runner]

        if left_val > curr_cube_length and right_val > curr_cube_length:
            print("No")
            return
        else:
            # determine which side is largest
            if left_val >= right_val and left_val <= curr_cube_length:
                curr_cube_length = left_val
                left_runner += 1
            elif right_val > left_val and right_val <= curr_cube_length:
                curr_cube_length = right_val
                right_runner -= 1
            else:
                print("No")
                return
    print("Yes")
    
# Enter your code here. Read input from STDIN. Print output to STDOUT
num_of_tests = int(input())

for i in range(num_of_tests):
    n = int(input())
    sideLengths = [int(num) for num in input().split()]
    myFunction(sideLengths)
