from user.models import User
def user_is_exits(email):
    try:
        use = User.objects.get(email=email,role=User.Role.FACULTY)
        return use
    except User.DoesNotExist:
        return False