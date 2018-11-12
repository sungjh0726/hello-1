class TestClass:
    name = "TEST"

    def __init__(self):
        print("TTTTTTTTTTTTTT")

    def static_method():
        print("STATIC!!")

    def get_name(self):
        print("QQQQQQQQQQQQQQQQQQQQ")
        return self.name

    def area(self, x, y):
        return x * y

class Child(TestClass):
    def __init__(self):
        super().__init__()
        print("My init!!!")

    def get_name(self):
        t = super().get_name()
        return "Child Name:" + self.name

    def area(self, x, y):
        t = super().area(x, y)
        return t / 2

test = TestClass()
child = Child()

getattr(test, 'get_name')()
getattr(TestClass, 'static_method')()

# print("11111>>", child.get_name())

# c = callable(test.get_name)
# print("cccccccc>>", c)
