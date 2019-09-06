space_str = "       \t\n\r"

print(space_str.isspace())

# num_str = "1.1"
# num_str = "\u00b2"
num_str = "九万九千九"

print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())
