from functools import reduce

#List comprised of 5 polygons
polygons = [[9, 12, 15], [8, 15, 17], [10, 10, 10], [4, 8, 4, 8], [7, 7, 7, 7]]

print("Polygons:", polygons)

#Function to add the sides of a polygon together
def poly_sum(polygon):
    perimeter = reduce(lambda a, b : a + b, polygon)
    return perimeter

#Uses list comprehension to pull one polygon from the list and give the perimeter
print("Perimeter of Polygons:", [poly_sum(x) for x in polygons])

#Uses list comprehension to filter out triangles from list
triangles = [x for x in polygons if len(x) == 3]

print("Triangles:", triangles)

#Function to determine if polygon is a right triangle
def right_triangle(polygon):
    (a, b, c) = sorted(polygon)
    return a**2 + b**2 == c**2

#Uses list comprehension to filter out only right triangles
right_tri = [x for x in triangles if right_triangle(x)]

print("Right Triangles:", right_tri)

#Uses list comprehension to map out and return the perimeter of right triangles
print("Perimeter of Right Triangles:", [poly_sum(x) for x in right_tri])