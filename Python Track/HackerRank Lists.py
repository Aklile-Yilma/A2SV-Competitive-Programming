if __name__ == '__main__':
    N = int(input())
    
numbers = []
for _ in range(N):
    
    commands = input().split()
    commandName = commands[0]
    
    if(commandName == 'insert'):
        numbers.insert(int(commands[1]), int(commands[2]))
    elif(commandName == 'print'):
        print(numbers)
    elif(commandName == 'remove'):
        numbers.remove(int(commands[1]))
    elif(commandName == 'append'):
        numbers.append(int(commands[1]))
    elif(commandName == 'sort'):
        numbers.sort()
    elif(commandName == 'pop'):
        numbers.pop()
    elif(commandName == 'reverse'):
        numbers.reverse()
        
