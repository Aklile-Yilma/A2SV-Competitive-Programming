def swap_case(s):
    
    letters = []
    for letter in s:
        if(letter.isupper()):
            letters.append(letter.lower())
        elif(letter.islower()):
            letters.append(letter.upper())
        else: 
            letters.append(letter)
    
    return ''.join(letters)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
