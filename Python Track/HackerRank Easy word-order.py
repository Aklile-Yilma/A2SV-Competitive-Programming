 
# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
size = int(input())

words = []

for i in range(size):
    words.append(input())

# dictionary of words and their number
count = collections.Counter(words)

print(len(count))
for value in count.values():
    print(value, end=' ')


