print("-----Program for printing student name with marks using list-----")

# create an empty dictionary
D = {}

#n = int(input('How many student record you want to store?? '))
n = 3
# create an empty list
# Add student information to the list
ls = []
lg = []
for i in range(0, n):
    # Take combined input name and
    # percentage and split values
    # using split function.
    #x = Students = ['student1', 'student2', 'student3', 'student4', 'student5', 'student6', 'student7', 'student8','student9', 'student10']
    #y =  Marks1 = [45, 78, 12, 14, 48, 43, 47, 98, 27, 80]
    x, y = input("Enter the student name and it's percentage: ").split()
    #x, y = .split(Students,Marks1)

    # Add name and marks stored in x, y
    # respectively using tuple to the list
    ls.append((y, x))
    lg.append((y, x))
# sort the elements of list
# based on marks
ls = sorted(ls, reverse=True)



# sort the elements of list
# based on marks
lg = sorted(lg, reverse=False)

print('Sorted list of students according to their marks in descending order')


#print('Sorted list of students according to their marks in descending order')

for i in ls:
    # print name and marks stored in
    # second and first position
    # respectively in list of tuples.
    print(i[1], i[0])

print()

for i in lg:
    # print name and marks stored in
    # second and first position
    # respectively in list of tuples.
    print(i[1], i[0])
print()
#for i in range(3):
if int(y) > 25 and int(y) < 75:
        #ls[i] = Marks
        #lf = sorted(lf, reverse=False)
    print(x, y)













# for i in range(10):
#     # Take combined input name and
#     # percentage and split values
#     # using split function.
#     Students = ['student1', 'student2', 'student3', 'student4', 'student5', 'student6', 'student7', 'student8','student9', 'student10']
#     Marks = [45, 78, 12, 14, 48, 43, 47, 98, 22, 80]
#
#     # Add name and marks stored in x, y
#     # respectively using tuple to the list
#     ls.append((Marks, Students))
#
# # sort the elements of list
# # based on marks
# str = ls = Marks = [45, 78, 12, 14, 48, 43, 47, 98, 22, 80]
# ls = sorted(ls, reverse=True)
#
# print('Sorted list of students according to their marks in descending order')
#
# for i in range(10):
#     if Marks>0 and Marks>100:
#     # print name and marks stored in
#     # second and first position
#     # respectively in list of tuples.
#     #Students = ['student1', 'student2', 'student3', 'student4', 'student5', 'student6', 'student7', 'student8','student9', 'student10']
#         print(Students[i],Marks[i])