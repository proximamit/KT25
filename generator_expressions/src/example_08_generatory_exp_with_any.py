# Stops at first weak password

# check if a list of passwords contains any entries shorter than 6 characters.

passwords = ["abc", "123456", "secret123"]

has_weak = any(
    len(p) < 6
    for p in passwords
)

print(has_weak)

# any(cond(x) for x in items)

'''
# Returns the first item that matches the condition
weak_pwd = next((p for p in passwords if len(p) < 6), None)
print(weak_pwd)
'''