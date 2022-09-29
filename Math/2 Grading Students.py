def gradingStudents(grades):

    myGrades=[]
    for grade in grades:
        rem= grade%5
        add=5-rem
        if(rem>=3 and grade>37):
            grade+=add
            myGrades.append(grade)
        else:
            myGrades.append(grade)
            

        
    return myGrades


grades=[73,67,38,33]

print(gradingStudents(grades))

