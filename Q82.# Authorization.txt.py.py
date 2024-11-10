import functools

def get_current_user_permissions():
    # Dummy implementation for illustration; replace with actual logic
    return ['user', 'admin']

def requires_permission(permission):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user_permissions = get_current_user_permissions()
            if permission in user_permissions:
                return func(*args, **kwargs)
            else:
                raise PermissionError("You do not have permission to access this resource.")
        return wrapper
    return decorator

@requires_permission('admin')
def delete_user(user_id):
    print(f"User {user_id} deleted")

# Example usage
try:
    delete_user(123)
except PermissionError as e:
    print(e)
print("THIS PROGRAM IS WRITTEN BY VAANI, ERP:-162")
