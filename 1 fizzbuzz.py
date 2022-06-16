class Solution(object):
    def fizzBuzz(self, n):
        
        fizz_array=[]
        for i in range(1,n+1):
            if(i%3==0 and i%5==0):
                fizz_array.append("FizzBuzz")
            elif(i%3==0):
                fizz_array.append("Fizz")
            elif(i%5==0):
                fizz_array.append("Buzz")
            else:
                fizz_array.append(str(i))
        
        return fizz_array

"""
class Solution:
    def fizzBuzz(self, n):
    
        # ans list
        ans = []

        for num in range(1,n+1):

            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)

            if divisible_by_3 and divisible_by_5:
                # Divides by both 3 and 5, add FizzBuzz
                ans.append("FizzBuzz")
            elif divisible_by_3:
                # Divides by 3, add Fizz
                ans.append("Fizz")
            elif divisible_by_5:
                # Divides by 5, add Buzz
                ans.append("Buzz")
            else:
                # Not divisible by 3 or 5, add the number
                ans.append(str(num))







"""