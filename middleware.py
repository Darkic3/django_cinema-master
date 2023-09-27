from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import redirect


class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user # Who is the current user ?
        if user.is_authenticated:
                return redirect(reverse('index-page'))
        else:
            if request.path == reverse('login_page') or modulename == 'django.contrib.auth.views':
                pass
            else:
                return redirect(reverse('login_page'))
