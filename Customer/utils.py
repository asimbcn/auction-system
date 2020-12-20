from .models import Customer, ShippingAddress
from Administrator.models import Product, Coupon
from datetime import datetime


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


def getProfile(request, pk='None'):
    if pk != 'None':
        customer = Customer.objects.get(id=pk)
        return customer
    else:
        user = request.user
        if user is not None:
            try:
                customer = Customer.objects.get(user=user)
                return customer
            except:
                return ''
        else:
            return ''


def getShipping(request):
    customer = getProfile(request)
    if customer != '':
        try:
            shipping = ShippingAddress.objects.get(customer=customer)
            return shipping
        except:
            return ''
    else:
        return ''


# def prodUpdate():
#     product = Product.objects.filter(status=True)
#     for p in product:
#         print(p)
#         print(datetime.date())
#         print(p.valid_time)
#         # if datetime.now() > p.valid_time:
#         #     print('change')
#         #     p.status = False
#         #     try:
#         #         prod.save()
#         #     except:
#         #         continue
