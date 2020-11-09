from .models import Customer


def check_permission(request):
    if request.user.customer.admin == False:
        return {'status': False}
    elif request.user.customer.admin == True:
        return {'status': True}
    else:
        return {'status': False}
