import random
from datetime import datetime

class Jiju:
    def __init__(self):
        self.traits = [
            "Multi-talented",
            "Smart",
            "Handsome",
            "Techie",
            "Awesome Human"
        ]

        self.age = random.randint(21, 41)
        ##print(f"{self.age}")
        #self.age = self.age + 1 if hasattr(self, 'age') else 1
        self.age = getattr(self, 'age', 0) + 1
        ##print(f"{self.age}")

    def get_birthday_suffix(self, age):
        # Handle special cases: 11th, 12th, 13th
        if 10 <= age % 100 <= 13:
            return "th"

        # Handle normal cases
        suffixes = {
            1: "st",
            2: "nd",
            3: "rd"
        }

        return suffixes.get(age % 10, "th")

    def birthday_message(self):

        chosen_suffix = self.get_birthday_suffix(self.age)

        print("Happy Birthday Jiju\n")

        for trait in self.traits:
            #print(f"Loading {trait}... Done!")
            #print(f"Loading {trait:<20}... Done!")
            print(f"{f'Loading {trait}...':<35} Done!")

        wishes = [
            "Success in every project",
            "Bug-free life :-)",
            "Unlimited happiness",
            "Good health",
            "Lots of love and laughter"
        ]

        print(
            f"\nOn your {self.age}{chosen_suffix} birthday, "
            f"Wishing you a year filled with:"
        )

        for wish in wishes:
            print(f"\n--> {wish}")

        print("\nSystem Status:")
        status = {
            "Happiness": "99%",
            "Celebration": "ON",
            "Weekend Mode": "ACTIVATED"
        }
        status["Happiness"] = "100%"
        for key, value in status.items():
            #print(f"\t{key}: {value}")
            print(f"\t{f'{key}':<15}: {value}")
        print("\nHave a splendid birthday weekend, Jiju!")


if __name__ == "__main__":
    myJiju = Jiju()
    today = datetime.now()
    if today.day == 17 and today.month == 5:
        myJiju.birthday_message()
    else:
        print(today)
