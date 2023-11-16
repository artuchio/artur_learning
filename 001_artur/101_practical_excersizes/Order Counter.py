def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

def calculate_total_material(order):
    total_carpet_material = 0
    total_edge_material = 0

    for item in order:
        size = item['size']
        width = item['width']
        height = item['height']
        qty = item['qty']

        total_carpet_material += calculate_area(width, height) * qty
        total_edge_material += calculate_perimeter(width, height) * qty

    return total_carpet_material, total_edge_material

order = [
    {'size': 'small', 'qty': 35, 'width': 0.6, 'height': 0.4},
    {'size': 'medium', 'qty': 20, 'width': 0.8, 'height': 0.6},
    {'size': 'large', 'qty': 15, 'width': 0.9, 'height': 0.9},
]

total_carpet, total_edge = calculate_total_material(order)

print(f"1. TOTAL CARPET MATERIAL {total_carpet} m2")
print(f"2. TOTAL EDGE MATERIAL {total_edge} m")
