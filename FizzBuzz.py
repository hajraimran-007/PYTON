#Given an integer n, return a list of strings from 1 to n where multiples of 3 are 'Fizz', multiples of 5 are 'Buzz', and multiples of both are 'FizzBuzz'.
i=30
result=[]
for n in range(1,i+1):
 if n%3==0 and n%5==0:
  result.append("fizzbuzz")  
 elif n%3==0:
  result.append("fizz")  
 elif n%5==0:
  result.append("buzz")
else:
 result.append(str(n)) 

print(result)

