t = float(input("Enter talents: "))
p = float(input("Enter pounds: "))
l = float(input("Enter lots: "))

total_grams = (((t * 20 + p) * 32) + l) * 13.3
kg = int(total_grams // 1000)
gr = total_grams % 1000
print(f"The weight in modern units: {kg} kilograms and {gr:.2f} grams.")