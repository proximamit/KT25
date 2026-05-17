import random 

class Jiju:
    def __init__(self):
        self.traits = [
            "Multi-talented",
            "Smart",
            "Handsome",
            "Techie",
            "Awesome Human"
        ]
        #self.age = 1
        self.age = random.randint(21, 41)
        #self.age += 1 if hasattr(self, 'age') else 1
        self.age = self.age + 1 if hasattr(self, 'age') else 1
        

    def birthday_message(self):
        print("Happy Birthday Jiju\n")
        for trait in self.traits:
            print(f"Loading {trait}... Done!")

        wishes = [
            "Success in every project",
            "Bug-free life :-)", 
            "Unlimited happiness",
            "Good health", 
            "Lots of love and laughter"
        ]
        print(f"\n On your Wishing you a year filled with:")
        for wish in wishes:
            print(f"\n--> {wish}")
        print("\nSystem Status: ")
        print("\tHappinss: 100%")
        print("\tCelebration: ON")
        print("\tWeekend Mode: ACTIVATED")
        print("\nHave a splendid birthday weekend, Jiju!")

if __name__ == "__main__":
    myJiju = Jiju()
    myJiju.birthday_message()

