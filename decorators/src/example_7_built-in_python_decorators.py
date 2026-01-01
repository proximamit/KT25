class MyClass:
    _value = 0

    @staticmethod
    def greet():
        print("Hello, static method!")

    @classmethod
    def set_value(cls, value):
        cls._value = value

    @property
    def value(self):
        return self._value

obj = MyClass()
obj.set_value(100)
print(obj.value)  # Calls the property method

MyClass.greet()  # Calls the static method
