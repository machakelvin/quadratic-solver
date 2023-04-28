import cmath
# at this moment i want need to accept the input from the user
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

# calculate the discriminant
# this is like the general formula for quadratic equation
d = (b ** 2) - (4 * a * c)

# find two solutions
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)
print('The solution are {0} and {1}'.format(sol1, sol2))