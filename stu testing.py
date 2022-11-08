import numpy as np

Students = ['student1','student2','student3','student4','student5','student6','student7','student8','student9','student10']
Marks = [45, 78, 12, 14, 48, 43, 47, 98, 22, 80]
# print(Students, Marks)




#lf = map(Marks.append(Students),Students)
#lf = sorted(lf, reverse=False)
#print(lf)
#stdData = []
#for Students, Marks in stdData:
  #  print(Students, Marks)
#lf = Marks
for i in range(10):
    if Marks[i] > 25 and Marks[i] < 75:
        #ls[i] = Marks
        #lf = sorted(lf, reverse=False)
        print(Students[i], Marks[i])
        # stdData = sorted(stdData, reverse=False)
print()

for i in range(5):
    if Marks[i] > 0 :
        lf = Marks
        #map(lf.append(Students), Students)
        # ls = Students
        # Students = sorted(Students, reverse=False)
        lf = sorted(lf, reverse=False)

        # ls = [Students[i],Marks[i]]
        # ls = sorted(ls,reverse=False)
        #map(Students.count, Students)
        #dict(zip(Students, map(Students.count, Students)))
        print(Students[i], lf[i])
print()
#map(Students.count, Students)

for i in range(5):
    sortedindexlist = np.argsort(Marks[i])
    if Marks[i] > 0:
 #       sorted(Students, key=lambda x: x[i])
        lf = Marks

        # ls = Students
        # Students = sorted(Students, reverse=False)
        lf = sorted(lf, reverse=True)
        # ls = [Students[i],Marks[i]]
        # ls = sorted(ls,reverse=False)
        print(Students[i], lf[i])

# def groupby(Students, Marks):


# student9 22
# student6 43
# student1 45
# student7 47
# student5 48

# student3 12
# student4 14
# student9 22
# student6 43
# student1 45
