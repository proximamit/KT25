# Writing Flexible APIs

def create_user(username, email, *args, **kwargs):
    user = {
        "username": username,
        "email": email,
    }

    if args:
        user["roles"] = args  # positional extra roles

    if kwargs:
        user.update(kwargs)  # dynamic attributes

    return user

u = create_user("john", "john@mail.com", "admin", "editor", age=25, active=True)
print(u)
