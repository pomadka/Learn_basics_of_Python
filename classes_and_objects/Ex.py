class Vehicle:
    name = ""
    kind = ""
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle()
car1.name = "BMW"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Volvo"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

print car1.description()
print car2.description()
