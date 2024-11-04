class human():

  def __init__(self, name, age, height):
    self.name = name
    self.age = age
    self.height = height


class car():

  def __init__(self, brand, model, topspeed):
    self.brand = brand
    self.model = model
    self.topspeed = topspeed


print("***HUMAN***")

person1 = human("Jonathan", 14, "180cm")
print("Name:", person1.name)
print("Age:", person1.age)
print("Height:", person1.height)

print("")
print("***CAR***")

car1 = car("Hyundai", "IONIQ 5", "185km/h")
print("Brand:", car1.brand)
print("Model:", car1.model)
print("Max Speed:", car1.topspeed)
