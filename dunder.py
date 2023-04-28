###
# Class creating and invocation
###


class Person:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __del__(self) -> None:
        print("Object Deconstructor")


p = Person("Sourabh", 25)

###
# Class using dunder to create a different representation
# for how the vector is presented
###


class Vector:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f" x = {self.x}, y = {self.y}"

    def __add__(self, other) -> __repr__:
        return Vector(self.x + other.x, self.y + other.y)

    def __call__(self):
        return print("I was called!")

vec1 = Vector(10,20)
vec2 = Vector(50,60)
vec3 = vec2 + vec1

print(vec3)
vec3()