from django.shortcuts import redirect,render
from functools import wraps



def dealer_login_required(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('dealer_login')  # Redirect to a login page if not authenticated
        if request.user.is_superuser or (hasattr(request.user, 'role') and request.user.role == 'DEALER'):
            return function(request, *args, **kwargs)  # Allow access if superuser or DEALER
        else:
            return render(request, "unauthorized.html")  # Render unauthorized page otherwise
    return wrapper
