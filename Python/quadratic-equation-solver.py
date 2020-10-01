import cmath;

print("Enter 'x' for exit.");
n1 = input("Enter value of a: ");

if n1 == 'x':
    exit();
else:
    n2 = input("Enter value of b: ");
    n3 = input("Enter value of c: ");
    num1 = float(n1);
    num2 = float(n2);
    num3 = float(n3);
    d = (num2**2) - (4*num1*num3);
    q1 = (-num2-cmath.sqrt(d))/(2*num1);
    q2 = (-num2+cmath.sqrt(d))/(2*num1);
    print("The solutions = {0} and {1}" .format(q1,q2));
