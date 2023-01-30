n, m = map(int, input().split())

road = []
S = (0, 0)
T = (0, 0)

def vertical(col, start, end):
    res = []
    for i in range(min(start, end), max(start, end) + 1):
        res.append(road[i][col])
    return res

def horizontal(row, start, end):
    res = road[row][min(start, end): max(start, end) + 1]
    return res

for row in range(n):
    road.append(list(input()))
    if 'S' in road[-1]:
        S = (row, road[-1].index('S'))
    if 'T' in road[-1]:
        T = (row, road[-1].index('T'))
boolean = True

if S[1] != T[1]:
    for row in range(len(road)):
        sliced = road[row][min(S[1], T[1]): max(S[1], T[1])+1]

        if '*' not in sliced:
            if ('*' not in vertical(S[1], S[0], row)) and ('*' not in vertical(T[1], T[0], row)):
                print('YES')
                boolean = False
                break

if boolean and T[0] != S[0]:
    for col in range(len(road[0])):
        sliced = vertical(col, S[0], T[0])
        if '*' not in sliced:
            if ('*' not in horizontal(S[0], S[1], col)) and ('*' not in horizontal(T[0], T[1], col)):
                print('YES')
                boolean = False
                break

if boolean:
    print('NO')