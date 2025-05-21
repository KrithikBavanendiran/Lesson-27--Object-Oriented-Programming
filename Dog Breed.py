class Dog:
   
    def __init__(self, breed):
        self.breed= breed

Tom=Dog("Labrador")
Tim=Dog("Golden retriver")

print("Tom is a {}".format(Tom.breed))
print("Tim is also a {}".format(Tim.breed))
