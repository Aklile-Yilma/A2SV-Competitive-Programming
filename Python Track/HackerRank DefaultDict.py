
from collections import defaultdict
n, m = map(int, input().split())


a_words = defaultdict(list)

for idx in range(n):
    a_words[input()].append(str(idx+1))

for idx in range(m):
    b_word = input()
    if(a_words[b_word]):
        print(' '.join(a_words[b_word]))
    else:
        print('-1')
