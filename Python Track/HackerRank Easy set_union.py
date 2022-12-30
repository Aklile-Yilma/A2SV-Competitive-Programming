english_subs = int(input())
english_students = set(input().split())
    
french_subs = int(input())
french_students = set(input().split(' '))

union = english_students.union(french_students)
union_subs = len(union)

print(union_s
