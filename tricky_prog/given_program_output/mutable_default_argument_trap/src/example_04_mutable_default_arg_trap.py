from dataclasses import dataclass
'''
@dataclass
class User:
    tags: list = []

user1 = User()
user2 = User()

user1.tags.append("admin")
print(user2.tags)

'''

"""
Output:

ValueError: mutable default <class 'list'> for field tags is not allowed: use default_factory

"""