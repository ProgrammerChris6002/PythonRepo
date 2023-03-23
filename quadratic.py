import math
def main():
    a = int(input("What's a? "))
    b = float(input("What's b? "))
    c = int(input("What's c? "))
    equation(a, b, c)


# x^2 - 5x - 14 = 0
# x^2 + 2x + 1 = 0
def equation(a, b, c):
    x1 = ((-b) + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
    x2 = ((-b) - math.sqrt((b * b) - (4 * a * c))) / (2 * a)
    print("x1 is equal to", x1)
    print("x2 is equal to", x2)

main()