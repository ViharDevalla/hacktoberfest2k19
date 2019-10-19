n=int(input('Enter a given number '))
sum=0
temp=n
while temp>0:
    digit= temp%10
    sum=digit**3+sum
    temp=temp//10
if n==sum:
    print(n,'is a Armstrong Number')
else:
    print(n,'is not a Armstrong Number')

    
    
