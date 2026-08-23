# Every Dog can conceptually attempt to run,
# but an injured Dog behaves differently.

class Dog:
    def __init__(self, name, injured=False):
        self.name = name
        self.injured = injured

    def run(self):
        if self.injured:
            self.limp()
        else:
            print(f"{self.name} is running.")

    def limp(self):
        print(f"\t{self.name} is limping.")


dog1 = Dog("Buddy")
dog2 = Dog("Max")
dog3 = Dog("Rocky", injured=True)

dog1.run()
dog2.run()
dog3.run()
