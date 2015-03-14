from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from mobiles.models import *
from random import randint
import random
import uuid
import smtplib
import json
import urllib2
from django.contrib.sessions.models import Session
from django.db.models import Q
from django.contrib import messages

from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    return render(request,"index.html")
    

def login(request):
    return render(request,"login.html") 


def contact_us(request):
    return render(request,"contact-us.html")

def mobiles_data(request):

    rand_mobi = mobiles.objects.values_list('pk',flat=True)
    select_mobi = random.sample(rand_mobi,3)
    most_liked = mobiles.objects.filter(pk__in =select_mobi)

    brands = mobiles.objects.values('brand').distinct()

    #all_data = mobiles.objects.values_list('pk',flat=True)
    #select_mobile = random.sample(all_data,20)
    #all_data1 = mobiles.objects.filter(pk__in =select_mobile)

    #all_data = mobiles.objects.all()
    all_data = mobiles.objects.filter(Q(brand='samsung')| Q(brand='htc')|Q(brand='apple')|Q(brand='micromax'))
    all_data = sorted(all_data, key=lambda x: random.random())
    paginator = Paginator(all_data, 21)

    page = request.GET.get('page')
    try:
        mobiles_data = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        mobiles_data = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        mobiles_data = paginator.page(paginator.num_pages)
    
    return render(request,"mobiles.html",{'data':brands,'all_data':mobiles_data,'liked':most_liked})    

def details(request,details):
    #return HttpResponse(details)
    pro_id = str(details)
    pro_id = details.split("/")[-1].strip()
    pro_id = str(pro_id)


    results = mobiles.objects.get(product_id=str(pro_id))
    #pro_model = results.model_name.replace(results.brand.lower(),"") 
    pro_model = results.model_name
    #all_data = mobiles.objects.filter(title__icontains=results.model_name.strip()).order_by('selling_price')     
    all_data = mobiles.objects.filter(model_name__exact=pro_model).order_by('selling_price')

    
    #return HttpResponse(all_data)
    rand_mobi = mobiles.objects.values_list('pk',flat=True)
    select_mobi = random.sample(rand_mobi,3)
    most_liked = mobiles.objects.filter(pk__in =select_mobi)

    if (len(all_data) ==0):
        all_data = mobiles.objects.filter(product_id=str(pro_id))
        data = all_data[0]
    else:    
        data = all_data[0]

    #data = mobiles.objects.get(product_id = pro_id)
    return render(request,"product-details.html",{'data':data,'liked':most_liked,'all_data':all_data})    


def category_brand(request,details):

    #return HttpResponse(request.build_absolute_uri())
    details = details.strip()
    brand1 = details.upper()

    brand_details = mobiles.objects.filter(brand = details)

    paginator = Paginator(brand_details, 21)

    page = request.GET.get('page')
    try:
        mobiles_data = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        mobiles_data = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        mobiles_data = paginator.page(paginator.num_pages)

    brands = mobiles.objects.values('brand').distinct()

    rand_mobi = mobiles.objects.values_list('pk',flat=True)
    select_mobi = random.sample(rand_mobi,3)    
    most_liked = mobiles.objects.filter(pk__in = select_mobi)

    
    return render(request,"brand-details.html",{'data':mobiles_data,'liked':most_liked,'brand_list':brands,'brand':brand1})    

def category_price(request,details):

    #return HttpResponse(request.build_absolute_uri())
    details = details.strip()
    price = details.split("-")

    start = price[0]
    end =price[1]
    
    #brand_details = mobiles.objects.filter(brand = details)
    
    #price_range = mobiles.objects.raw('SELECT * FROM mobiles_mobiles where selling_price between 1000 and 10000 ')
    #price_range1 = mobiles.objects.raw(('SELECT * FROM mobiles_mobiles where selling_price between %s and %s ')%(start,end))
    
    price_range1=mobiles.objects.filter(selling_price__gte=start).filter(selling_price__lte=end)
      
    paginator = Paginator(price_range1, 21)

    page = request.GET.get('page')
    try:
        mobiles_data = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        mobiles_data = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        mobiles_data = paginator.page(paginator.num_pages)


    brand_list =[]
    for brand1 in price_range1:
        brand_list.append(brand1.brand)
        
    
    unique_brand = set(brand_list)


    rand_mobi = mobiles.objects.values_list('pk',flat=True)
    select_mobi = random.sample(rand_mobi,3)    
    most_liked = mobiles.objects.filter(pk__in = select_mobi)

    
    return render(request,"price-details.html",{'data':mobiles_data,'brand':unique_brand,'liked':most_liked,'price_range':details})    

def category_price_brand(request,details,brand_details):
    info =[details,brand_details]
    #return HttpResponse(info)
    details = details.strip()
    price_details = details

    price = details.split("-")

    start = price[0]
    end =price[1]
    brand_details = str(brand_details.strip())


    
    #brand_details = mobiles.objects.filter(brand = details)
    
    #price_range = mobiles.objects.raw('SELECT * FROM mobiles_mobiles where selling_price between 1000 and 10000 ')
    #price_range1 = mobiles.objects.raw((""" SELECT * FROM mobiles_mobiles where (selling_price between %s and %s) and (brand = %s) """)%(start,end,brand_details))
    price_range1=mobiles.objects.filter(selling_price__gte=start).filter(selling_price__lte=end).filter(brand__icontains=brand_details)
    #price_range =price_range1[:21]  

    paginator = Paginator(price_range1, 21)

    page = request.GET.get('page')
    try:
        mobiles_data = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        mobiles_data = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        mobiles_data = paginator.page(paginator.num_pages)


    brand_range=mobiles.objects.filter(selling_price__gte=start).filter(selling_price__lte=end)
    brand_list =[]
    for brand1 in brand_range:
        brand_list.append(brand1.brand)
        
    
    brand_list = set(brand_list) 
    
    
    #brands_list = set(brand_list)


    rand_mobi = mobiles.objects.values_list('pk',flat=True)
    select_mobi = random.sample(rand_mobi,3)    
    most_liked = mobiles.objects.filter(pk__in = select_mobi)

    
    return render(request,"price_brand_details.html",{'data':mobiles_data,'brand_list':brand_list,'liked':most_liked,'cur_brand':brand_details,'price_detail':price_details})


def mobileSearch(request):
    if 'search' in request.GET and request.GET['search']:
        
        q = request.GET['search']
        messages.success(request, q)

        mobile = mobiles.objects.filter(Q(title__icontains=q.lower()) |Q(seller__exact=q.lower())|Q(brand__icontains=q.lower())|Q(model_name__icontains=q.lower()))
         
        brands = mobiles.objects.values('brand').distinct()

        rand_mobi = mobiles.objects.values_list('pk',flat=True)
        select_mobi = random.sample(rand_mobi,3)    
        most_liked = mobiles.objects.filter(pk__in = select_mobi)
 
        if (len(mobile)==0):
             return HttpResponseRedirect('/searchError/')

        return render(request, 'search_results_mobile.html',
            {'data': mobile, 'query': q,'brand':brands,'liked':most_liked})
    else:
        return HttpResponseRedirect('/searchError/')

def searchError(request):
    
    rand_mobi = mobiles.objects.values_list('pk',flat=True)
    select_mobi = random.sample(rand_mobi,3)
    most_liked = mobiles.objects.filter(pk__in =select_mobi)

    brands = mobiles.objects.values('brand').distinct()

    all_data = mobiles.objects.values_list('pk',flat=True)
    select_mobile = random.sample(all_data,20)
    all_data1 = mobiles.objects.filter(pk__in =select_mobile)
    
    return render(request,"searchError.html",{'data':brands,'all_data':all_data1,'liked':most_liked})
