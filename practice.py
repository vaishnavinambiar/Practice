num1 = int(raw_input("Enter the first number: "))
num2 = int(raw_input("Enter the second number: "))

def add_num(a,b):
    sum = a + b
    return sum
print "The sum is", add_num(num1, num2)


def sub_num(a,b):
     diff = a - b
     return diff
print "The difference is", sub_num(num1, num2)


def mul_num(a,b):
    prod = a * b
    return prod
print "The product is", mul_num(num1, num2)


def div_num(a,b):
    quot = a / b
    return quot
print "The quotient is", div_num(num1, num2)
