# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:23:49 2022

@author: happy
"""

Name_of_Subjects = []
Credit_hours = []
Marks_Obtained = []

# First loop to take all the inputs from the user
for i in range(4):
    Name_of_Subject = input("Enter Subject Name: ")
    Name_of_Subjects.append(Name_of_Subject)
    
    Credit_hours_of_subject = float(input("Enter Subject Credit Hours: "))
    Credit_hours.append(Credit_hours_of_subject)
    
    Marks_obtained_in_each_subject = int(input("Enter Obtained Marks: "))
    Marks_Obtained.append(Marks_obtained_in_each_subject)

GPA = [] 
# Second Loop to calculate the gpa of each subject 
for i in Marks_Obtained:
    marks = (i / 100) * 100
    
    if marks >= 90:
        GPA.append(4.0)
        print(marks, ".You got A grade.WOW !GREAT JOB DUDE.Topper(HAHA) !!")
    elif marks >= 85 and marks <= 89:
        GPA.append(3.7)
        print(marks, ".You got A- grade.AWESOME !")
    elif marks >= 80 and marks <= 84:
        GPA.append(3.3)
        print(marks, ".You got B+ grade.SUPER.")
    elif marks >= 75 and marks <= 79:
        GPA.append(3.0)
        print(marks, ".You got B grade.GOOD!")
    elif marks >= 70 and marks <= 74:
        GPA.append(2.7)
        print(marks, ".You got B- grade.GOOG TRY")
    elif marks >= 65 and marks <= 69:
        GPA.append(2.3)
        print(marks, ".You got C+ grade.TRY MORE.")
    elif marks >= 60 and marks <= 64:
        GPA.append(2.0)
        print(marks, ".You got C- grade.WORK HARD MORE.")
    else:
        GPA.append(0)
        print(marks, ".You got F grade.BETTER LUCK NEXT TIME.")
        
print("GPA_of_all_subjects: " + str(GPA))


Subject_Grade_Points = []
# Third Loop to find the Subject Grade Points
for credit,gpa in zip(Credit_hours, GPA):
    grade_point = round((credit * gpa),2)
    Subject_Grade_Points.append(grade_point)

print("Subject_Grade_Points: ", Subject_Grade_Points)

# take sum 
Grade_point_of_all_Subjects = sum (Subject_Grade_Points)
Total_Credit_Hours = sum (Credit_hours)

# Semester GPA Calculation
# round command will round off the semester gpa upto 2 decimal points
Semester_GPA = Grade_point_of_all_Subjects / Total_Credit_Hours
Semester_GPA = round(Semester_GPA, 2)
print("Semester_GPA: " + str(Semester_GPA))
print("ALL THE BEST FOR FUTURE.Thank you!!")

#Done by swetha G