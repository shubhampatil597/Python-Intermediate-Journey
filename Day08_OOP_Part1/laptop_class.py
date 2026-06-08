class Laptop:

    def __init__(self, brand, ram, processor):

        self.brand = brand
        self.ram = ram
        self.processor = processor

l1 = Laptop(
    "Dell",
    "16GB",
    "Intel i7"
)

print("Laptop Information")
print("------------------")

print("Brand:", l1.brand)
print("RAM:", l1.ram)
print("Processor:", l1.processor)