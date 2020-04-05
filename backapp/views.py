from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.http.response import HttpResponseForbidden, HttpResponse, JsonResponse, HttpResponseServerError
from backapp.models import Account, Item, LiveModel
from functools import wraps
import re

def check_login(f):
    @wraps(f)
    def inner(request,*arg,**kwargs):
        if request.session.get('is_login')=='1':
            return f(request,*arg,**kwargs)
        else:
            return HttpResponse(status=401)
    return inner

# Create your views here.
def text_validation(string):
    pattern = re.compile('^[0-9A-Za-z_]+$')
    return re.match(pattern, string) != None and len(string) >= 6 and len(string) <= 18

def check_username(username):
    try:
        user = Account.objects.get(username=username)
    except:
        return False
    return True

@require_http_methods(["POST"])
def register(request):
    params = request.POST
    if((not 'username' in params) or (not 'password' in params)):
        return HttpResponseForbidden()
    if((not text_validation(params['username'])) or (not text_validation(params['password']))):
        return HttpResponseForbidden()
    if(check_username(params['username'])):
        return JsonResponse({'status': False})
    account = Account()
    account.username = params['username']
    account.password = params['password']
    if('phone' in params):
        try:
            account.phone = int(params['phone'])
        except:
            account.phone = 0
    if('email' in params):
        account.email = params['email']
    if('province' in params):
        account.province = params['province']
    if('city' in params):
        account.city = params['city']
    if('region' in params):
        account.region = params['region']
    if('address' in params):
        account.address = params['address']
    account.save()
    return JsonResponse({'status': True})
 
@require_http_methods(["GET"])
def has_username(request):
    params = request.GET
    if((not 'username' in params) or (not text_validation(params['username']))):
        return HttpResponseForbidden()
    return JsonResponse({'status': check_username(params['username'])})
 
@require_http_methods(["POST"])
def login(request):
    params = request.POST
    print(params)
    if((not 'username' in params) or (not 'password' in params)):
        return HttpResponseForbidden()
    if((not text_validation(params['username'])) or (not text_validation(params['password']))):
        return HttpResponseForbidden()
    if(not check_username(params['username'])):
        return JsonResponse({'status': 1, 'message': 'Username not found'})
    account = Account.objects.filter(username=params['username'],password=params['password'])
    if account:
        request.session['is_login'] = '1'
        request.session['username'] = account.first().username
    return JsonResponse({'status': 0, 'message': 'Login successfully', 'account':{
        'username': account.first().username,
        'password': account.first().password,
        'email': account.first().email,
        'name': account.first().name,
        'address': account.first().address,
        'province': account.first().province,
        'city': account.first().city,
        'region': account.first().region,
        'phone': account.first().phone,
        'money': account.first().money,
        'has': account.first().has,
        'cart': account.first().cart,
    }})

@check_login
@require_http_methods(["POST"])
def change_account(request):
    params = request.POST
    user = request.session['username']
    account = Account.objects.get(username = user)
    if((not text_validation(params['password']))):
        return HttpResponseForbidden()
    account.password = params['password']
    if('phone' in params):
        try:
            account.phone = int(params['phone'])
        except:
            account.phone = 0
    if('email' in params):
        account.email = params['email']
    if('province' in params):
        account.province = params['province']
    if('city' in params):
        account.city = params['city']
    if('region' in params):
        account.region = params['region']
    if('address' in params):
        account.address = params['address']
    account.save()
    return JsonResponse({'status': True, 'account': {
        'username': account.username,
        'password': account.password,
        'email': account.email,
        'name': account.name,
        'address': account.address,
        'province': account.province,
        'city': account.city,
        'region': account.region,
        'phone': account.phone,
        'money': account.money,
        'has': account.has,
        'cart': account.cart,
    }})

@check_login
@require_http_methods(["GET"])
def logout(request):
    request.session['is_login'] = '0'
    return HttpResponse()

@require_http_methods(["GET"])
def all_pets(request):
    pass
    return redirect('/index/')

@require_http_methods(["POST"])
def search(request):
    pass
    return redirect('/index/')