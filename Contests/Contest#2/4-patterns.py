 
n = int(input())


answer = ''
answer_length = 0


for _ in range(n):
    pattern = input()
    answer_length = len(pattern)

    for idx, char in enumerate(pattern):
        #intial word setup
        if(len(answer) != answer_length):
            answer += char
        elif(answer[idx] == '?'):
            answer = answer[:idx] + char + answer[idx+1:]

        elif(answer[idx]==char or answer[idx] == '!'):
            continue
        elif(answer[idx] != char):
            answer = answer[:idx] + '!' + answer[idx+1:]


print(answer)

