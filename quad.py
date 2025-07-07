import math

def solve(a, b, c):
    d= b**2 - 4*a*c  

    if d> 0:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        return f"Roots are real and distinct: {root1:.2f}, {root2:.2f}"
    elif d== 0:
        root = -b / (2 * a)
        return f"Roots are real and equal: {root:.2f}"
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(d)) / (2 * a)
        return f"Roots are complex: {real_part:.2f} ± {imaginary_part:.2f}i"

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

result = solve(a, b, c)
print(result)


