from dataclasses import dataclass, field

@dataclass
class User:
    tags: list = field(default_factory=list)

user1 = User()
user2 = User()

user1.tags.append("admin")

print(user1.tags)  # Output: ['admin']
print(user2.tags)  # Output: []
