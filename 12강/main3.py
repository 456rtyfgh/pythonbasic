class Animal:
    def eat(self):
        print ('먹는다')

    def move(self):
        print('움직이다')

class Dog(Animal):
    def bark(self):
        print('멍멍')

    def shake(self):
        print('꼬리를 흔들다')
        #210609

dog = Dog()
dog.eat()
dog.bark()
dog.shake()
dog.move()

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print ('먹는다')

    def move(self):
        print('움직이다')

class Dog(Animal):
    def __init__(self, name, age, owner):
        super().__init__(name, age)
        self.owner = owner
    def bark(self):
        print('멍멍')

    def shake(self):
        print('꼬리를 흔들다')
    
    def __str__(self) :
        sentence = '이름 : {}, 나이 : {}, 주인 : {}'.format(self.name, self.age, self.owner)
        return sentence
dog = Dog('포포', 15, '최준우')
print(dog)

class bird(Animal):
    

    def move(self):
        print('움직이다')

class bird(Animal):
    def __init__(self, name, age, owner):
        super().__init__(name, age)
        self.owner = owner
    def move (self):
        print('날다')

    def 쪼다(self):
        print('쪼다')
    
    def __str__(self) :
        sentence = '이름 : {}, 나이 : {}, 주인 : {}'.format(self.name, self.age, self.owner)
        return sentence

bird = bird('두리', 5, '최준우')
print(bird)

class 사람:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def 인간어 (self):
        print ('인간어')

    def __str__(self) :
            sentence = '이름 : {}, 나이 : {}'.format(self.name, self.age)
            return sentence

사람1 = 사람('사람의 이름', 10)
print(사람1)
class 선생님(사람):
    def __init__(self, name, age):
        super().__init__(name, age)

    def 가르침 (self):
        print ('가르침')

    def __str__(self) :
            sentence = '이름 : {}, 나이 : {}'.format(self.name, self.age)
            return sentence

선생님1 = 선생님('선생님의 나이', '선생님의 나이' )
print(선생님1)
class 학생(사람):
    def __init__(self, name, age):
        super().__init__(name, age)

    def 공부함 (self):
            print ('공부함')
    
    def __str__(self) :
            sentence = '이름 : {}, 나이 : {}'.format(self.name, self.age)
            return sentence

학생1 = 학생('최준우', 12)
print(학생1)
