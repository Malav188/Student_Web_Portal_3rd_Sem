from django.shortcuts import render
from django.urls import reverse

from user.models import Faculty,User
def user_is_exits(email):
    try:
        use = Faculty.objects.get(email=email,role=User.Role.FACULTY)
        return use
    except User.DoesNotExist:
        return False


def login_not_required_restric(func):
    def wrapper(request):
        if request.user.is_authenticated:
            return render(request, 'faculty/login.html', {
                'link_title': 'signout',
                'link_message': 'you are arlady login with a account please logout first to login again or go to home page',
                'link1_url': reverse('faculty signout'),
                'link1_name': 'signout',
                'link2_url': reverse('faculty home'),
                'link2_name': 'home'
            })
        else:
            return func(request)
    return wrapper