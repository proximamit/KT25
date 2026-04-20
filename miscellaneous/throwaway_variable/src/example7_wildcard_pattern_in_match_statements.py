
# In Python 3.10+
# the underscore serves as a wildcard pattern in match statements.

def check_status(status_code):
    match status_code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown"
        
print(check_status(301))
print(check_status(200))
