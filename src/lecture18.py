# using + to add strings together
my_name = "Jorijn"
print("Hello " + my_name)

# using the .format() method
print("Hello {}".format(my_name))
print("The {2} {0} {1}".format("brown", "fox", "quick"))
print("The {q} {b} {f}".format(b="brown", f="fox", q="quick"))

# using .format() to clean up floats
result = 100 / 777
# {varname : width . precision f} (no spaces)
print("100 / 777 = {r:1.3f}".format(r=result))

# using formatted string literals
print(f"Hello {my_name}")
