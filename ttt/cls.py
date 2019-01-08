class Parent:
    name = '부모이름'
    def __str__(self):
        print(locals())
        return "toStr: '{}'".format(self.name)
    
    def get_name(self):
        return "This is " + self.name

    @classmethod
    def class_method(Parent):
        print("TTTTTTTTTTTTTTTT", Parent.name)

    @property
    def nm(self):
        return self.name

    @staticmethod
    def full_name():
        print("NAME: " + Parent.name)

    def small_name():
        print("Small!!!")

class Child(Parent):
    name = "자식이름"
    def get_name(self):
        t = super().get_name()
        return t + "@@@@@"

print("::::::::::::::::>>", __name__)  # 이파일이 실행되면 '__main__' 값!
p = Parent()
print("p=", p, dir(p))
print(p.get_name(), Parent.name, p.name)
print("nm=", p.nm)

Parent.class_method()
p.name = "new name"
p.class_method()

p.full_name()
Parent.full_name()
Parent.small_name()

c = Child()
print("YYY>>", c.get_name())