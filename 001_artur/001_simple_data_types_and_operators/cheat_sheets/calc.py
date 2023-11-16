# Вычислить плошад треугольника
side_a = float(input("enter side A: "))
side_b = float(input("enter side B: "))
side_c = float(input("enter side C: "))

half_perimetr = (side_a + side_b + side_c) / 2
#inogda polezno pereproverit' kod
# print(half_perimetr)
area = (half_perimetr *
        (half_perimetr - side_a) *
        (half_perimetr - side_b) *
        (half_perimetr - side_c)) ** 0.5
print("Area of triangle is: " + str(area))