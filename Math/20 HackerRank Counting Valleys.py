 
def countingValleys(steps, path):
    # Write your code here
    state = 0
    InValley = 0
    InValleyState = False

    for i in path:
        if(i == 'D'):
            state-=1
        else:
            state+=1

        if(state < 0 and InValleyState==False):
            InValley+=1
            InValleyState=True
        elif(state>=0):
            InValleyState=False


    return InValley
