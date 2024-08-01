from django.shortcuts import redirect,render


# def super_login_required(function):
#     def wrappeer(request,*args,**kwargs):
#         if not request.user.is_authenticated:
#             return redirect('dealer_login')
#         else:
#             if request.user.role != 'DEALER':
#                 return render(request, "unauthorized.html")
#         return function(request,*args,**kwargs)
#     return wrappeer