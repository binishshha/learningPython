check= lambda x:'positive' if x>0  else ('negative' if x<0 else 'zero')
print(check(0))

expression= lambda x: 'even' if x%2==0 else 'odd'
print(expression(6))

grade= lambda x: ('Distinction' if x>=80 else 'First Division' if x>=70 else'Second Division' if x>=60 else 'Fail')
mark = float(input("enter the marks: "))
print(grade(mark))