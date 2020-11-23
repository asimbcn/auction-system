from .models import Customer
from Administrator.models import Product


def check_permission(request):
    if request.user.customer.admin == False:
        return {'status': False}
    elif request.user.customer.admin == True:
        return {'status': True}
    else:
        return {'status': False}


def getProduct(request):

    try:
        allProd = Product.objects.all()
    except:
        allProd = ''

    try:
        activeProd = Product.objects.filter(status=True)
    except:
        activeProd = ''

    try:
        inactiveProd = Product.objects.filter(status=False)
    except:
        inactiveProd = ''

    return {
        'allProd': allProd,
        'activeProd': activeProd,
        'inactiveProd': inactiveProd
    }
