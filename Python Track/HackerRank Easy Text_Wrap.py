import textwrap

def wrap(string, max_width):
    result = ''
    for idx, char in enumerate(string):
        result += char 
        if((idx+1)%max_width == 0):
            result += '\n'
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
