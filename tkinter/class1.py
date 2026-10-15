class Cat:
    def __init__(self,breed,color,age):
        self.__breed = breed
        self.__color = color
        self.__age = age

    def meow(self):
        print('Мяу!')

    def get_breed(self):
        return self.__breed
    

c = Cat('Русская голубая','Черный',5)

print(c.get_breed())
