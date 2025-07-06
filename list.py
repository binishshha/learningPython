lists = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lambda_list = list(map(lambda x: x**2, lists))
print(lambda_list)
print(sum(lambda_list))
 
lambdaevenlist= list(filter(lambda x: x % 2==0, lists))
lambaoddlist= list(filter(lambda x: x % 2!=0, lists))
print(lambdaevenlist)
print(lambaoddlist)