# Take P, N and R as input from user
p=float(input('Please enter Principal in INR :'))
n= float(input('Please enter Period in Years :'))
r=float(input ('Please enter Rate of Interest in %p.a. :'))
# Calculate Compund interest amount 
a=p*(1+r/100)**n
i = a - p
# Print above results
print(f'Amount for Compound Interest : {a:.2f} INR')
print (f'Total Interest : {i:.2f INR}')