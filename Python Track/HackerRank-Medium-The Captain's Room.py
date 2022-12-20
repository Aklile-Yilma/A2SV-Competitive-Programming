# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections


size_of_group = int(input())
room_list = input().split(' ')

# count how many times a room number appears
count = collections.Counter(room_list)


for key in count.keys():
    #  if room number size is not equal to the size of the group, print captain's room
    if(count[key] != size_of_group):
        print(key)

