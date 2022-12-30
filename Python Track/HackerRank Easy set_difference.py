# Enter your code here. Read input from STDIN. Print output to STDOUT

english_subs = int(input())
english_students = set(input().split())
    
french_subs = int(input())
french_students = set(input().split(' '))

english_only_subs = 0

for roll_no in english_students:
    if(roll_no not in french_students):
        english_only_subs += 1
        
print(english_only_subs)
