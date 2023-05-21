# Придумать класс и методы к нему, использовать инкапсуляцию, полиморфизм и наследование


class Animal:
    def __init__(self, size, name, color):
        self.size = size
        self.name = name
        self.__color = color

    def move(self):
        return self.name + " " + "move"

    def eat(self):
        return "eat"


class Butterfly(Animal):
    def fly(self):
        return self.name + " " + "flies"

    def climb(self):
        return self.__color + " " + "climbs"

    def eat(self):
        return self.name + " " + self.size + " " + "eat"


class Beatle(Animal):
    def sound(self):
        return self.name + " " + "zzzzzzzzzzzz"

