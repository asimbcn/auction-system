from .models import Customer
from Administrator.models import Product, Coupon


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


def getCoupon(request):

    try:
        allCoup = Coupon.objects.all()
    except:
        allCoup = ''

    try:
        activeCoup = Coupon.objects.filter(active=True)
    except:
        activeCoup = ''

    try:
        inactiveCoup = Coupon.objects.filter(active=False)
    except:
        inactiveCoup = ''

    return {
        'allCoup': allCoup,
        'activeCoup': activeCoup,
        'inactiveCoup': inactiveCoup
    }