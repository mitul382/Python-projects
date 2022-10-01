print('<< Quadratic calculator >>')
print('Syntax: ax^2 + bx + c')
print('*********************')


a = float(input('Input the value of a: '))
b = float(input('Input the value of b: '))
c = float(input('Input the value of c: '))


difference = (b ** 2) - (4 * a *c)
root = difference ** 0.5
x1 = (-b + root) / (2 * a)
x2 = (-b - root) / (2 * a)
print('The roots of the equation are: ', x1, x2)
