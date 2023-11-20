from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def cart_details(request,tot=0,count=0,cart_items=None):
    try:
        ct=cartlist.objects.get(cart_id=cart_id(request))
        cart_items=items.objects.filter(cart=ct,active=True)
        for i in cart_items:
            tot +=(i.prodt.price*i.quan)
            count+=i.quan
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'ci':cart_items,'t':tot,'cn':count})

def cart_id(request):
    cart_id=request.session.session_key
    if not cart_id:
        cart_id=request.session.create()
    return cart_id

def add_cart(request,product_id):
    prod=products.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=cart_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=cart_id(request))
        ct.save()
    try:
        cart_items=items.objects.get(prodt=prod,cart=ct)
        if cart_items.quan < cart_items.prodt.stock:
            cart_items.quan+=1
        cart_items.save()
    except items.DoesNotExist:
        cart_items=items.objects.create(prodt=prod,quan=1,cart=ct)
        cart_items.save()
    return redirect('cartDetails')

def min_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=cart_id(request))
    prod=get_object_or_404(products,id=product_id)
    cart_items=items.objects.get(prodt=prod,cart=ct)
    if cart_items.quan>1:
        cart_items.quan-=1
        cart_items.save()
    else:
        cart_items.delete()
        return redirect('cartDetails')

def cart_delete(request,product_id):
    ct=cartlist.objects.get(cart_id=cart_id(request))
    prod=get_object_or_404(products,id=product_id)
    cart_items=items.objects.get(prodt=prod,cart=ct)
    cart_items.delete()
    return redirect('cartDetails')
       
