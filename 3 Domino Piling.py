def maxPileFinder():
    x,y=input("enter the pile sides with space: ").split()
    total_piles= int(x)*int(y)
    return total_piles//2

print(maxPileFinder())