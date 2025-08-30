#This program tells grade
s=float(input('marks of math: '))
s1=float(input('marks of science: '))
s2=float(input('marks of social science: '))
s3=float(input('marks of english: '))
s4=float(input('marks of hindi: '))
total_marks=s+s1+s2+s3+s4
percentage=total_marks/5.0
if percentage>=90:
    print('Grade A')
elif percentage>=80 and percentage<90:
    print('Grade B')
elif percentage>=70 and percentage<80:
    print('Grade C')
elif percentage>=60 and percentage<70:
    print('Grade D')
elif percentage>=40 and percentage<60:
    print('Grade E')
else:
    print('grade F')
    

          
