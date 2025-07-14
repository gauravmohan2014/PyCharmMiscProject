stdnt_dict = {'Stdnt1':100,'Stdnt2':99, 'Stdnt3':98, 'Stdnt4':97, 'Stdnt5':96}
stdnt_name = input("Enter the student's name: ")
try:
    stdnt_marks = stdnt_dict[stdnt_name]
    print(stdnt_name + "'s marks: " + str(stdnt_marks))
except:
    print('Student not found.')