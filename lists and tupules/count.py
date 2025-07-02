#tuples are immutable i.e elements cannot be modified
gradeList= ('C','D','A','A','B','B','A')
count=gradeList.count('A')
print(count)


#lists
gradeList= ['C','D','A','A','B','B','A']
print(gradeList)
gradeList.sort()
print(gradeList[6])
gradeList[6]='NEW'
print(gradeList[6])
print(gradeList)
gradeList.sort(reverse=True)
print(gradeList)
