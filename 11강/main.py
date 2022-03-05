class Dog:
    name = '코코'
    age = 2

    def bark(self):
        print('멍멍')
         
    def move(self):
        print('움직이다')

dog1 = Dog()
dog1.name = '코코'
dog1.age = 2

dog2 = Dog()
dog2.name = '두리'
dog2.age = 4
dog2.weight = 10

print(dog1.name, dog1.age)
print(dog2.name, dog2.age)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('{}가 멍멍'.format(self.name))
         
    def move(self):
        print('{}가 움직이다'.format(self.name))

dog1 = Dog('코코', 2)
dog2 = Dog('두리', 4)
dog1.bark()
dog2.bark()
dog1.move()
dog2.move()
print(dog1.name, dog1.age)
print(dog2.name, dog2.age)


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('{}가 멍멍'.format(self.name))
         
    def move(self):
        print('{}가 움직이다'.format(self.name))
    
    def __str__(self):
        sentence = '이름:{}, 나이:{}'.format(self.name, self.age)
        return sentence

dog1 = Dog('코코', 2)
dog2 = Dog('두리', 4)
print(dog1)
