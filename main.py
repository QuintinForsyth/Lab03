import math



# print_division_info(4, 3)  # should print: 4 divided by 3 is 1 remainder 1
# print_division_info(42, 12)  # should print: 42 divided by 12 is 3 remainder 6
def print_division_info(num1, num2):
  div = math.floor(num1/num2) 
  rem = num1%num2 # % is to find the remainder its called modulus
  print(str(num1) + " divided by "+ str(num2)+ " is "+str(div)+ " and the remainder is "+str(rem) )


def solve_quadratic(a, b, c):
  x1 = b + math.sqrt(b ** 2  - (4*a*c))/(2*a)
  x2 = b - math.sqrt(b ** 2 - (4*a*c))/(2*a)
  print("The roots of y = "+str(a)+"x^2 + "+str(b)+"x + "+str(c)+" are "+str(x1)+" and "+str(x2))


  
print("Part 1")
num1 = 42
num2 = 12
print_division_info(num1, num2)

print("Part 2")
solve_quadratic(4, 6, 9)



