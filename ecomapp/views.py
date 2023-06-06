from django.shortcuts import render,redirect
from django.http import HttpResponse
from ecomapp.models import Product
from django.db.models import Q
from ecomapp.forms import EmpForm,ProductModelForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def home(request):
    #data=Product.objects.all() ;active and inactive
    #print(data)
    data=Product.objects.filter(status=1)#fetch only active products
    content={}
    content['products']=data
    return render(request,'index.html',content)

def delete(request,rid):
    print("Id to be deleted:",rid)
    return HttpResponse("Id to be deleted:"+rid)

def edit(request,rid):
    print("Id to be edited is:",rid)
    return HttpResponse("Id to be edited:"+rid)

def addition(request,x,y):
    z=int(x)+int(y)
    print("Addition is:",z)
    return HttpResponse("Addition is:"+str(z))
'''
def User_register(request):
    return render(request,'register.html')
'''  


def product_list(request):
    context={}
    context['name']="Iphone"
    context['x']=100
    context['y']=200
    context['data']=[10,20,30,40,50]
    #context['plist']=['Iphone','samsung','Nokia','vivo','realme']
    context['plist']=[
                      {'name':'Samsung','pimage':'image of product','price':30000,'desc':'Product description'},
                      {'name':'iphone','pimage':'image of product','price':50000,'desc':'Product description'},
                      {'name':'vivo','pimage':'image of product','price':40000,'desc':'Product description'},
                      
                      ]
    return render(request,'productlist.html',context)

def reuse(request):
    return render(request,'base.html')

#sorting start
def sort(request,sv):
    if sv=='0':
        param='price'
    else:
        param='-price'
    data=Product.objects.order_by(param).filter(status=1)
    content={}
    content['products']=data
    return render(request,'index.html',content)  

def catfilter(request,catv):
    q1=Q(cat=catv)
    q2=Q(status=1)
    data=Product.objects.filter(q1 & q2)
    content={}
    content['products']=data
    return render(request,'index.html',content)

def pricefilter(request,pv):
    q1=Q(status=1)
    if pv=="0":
        q2=Q(price__lt=5000)
    else:
        q2=Q(price__gte=5000)

    data=Product.objects.filter(q1 & q2) 
    content={}
    content['products']=data
    return render(request,'index.html',content) 

def  pricerange(request):

    low=request.GET['min']
    high=request.GET['max']
    #print(low)
    #print(high)     
    #select * from ecomapp_product where price>=low and price<=high and status=1;
    q1=Q(status=1)
    q2=Q(price__gte=low)
    q3=Q(price__lte=high)
    data=Product.objects.filter(q1 & q2 & q3)
    content={}
    content['products']=data
    return render(request,'index.html',content)

def product_details(request,pid):
    #print("id",pid)
    data=Product.objects.filter(id=pid)
    content={}
    content['products']=data
    return render(request,'product_details.html',content)

def addproduct(request):
    #print("Method:",request.method)
    if request.method=="POST":
        #print("Insert record into database")
        #insert record into database table product
        n=request.POST['pname']
        c=request.POST['pcat']
        amt=request.POST['pprice']
        s=request.POST['status']
        #print(n)
        #print(cat)
        #print(amt)
        #print(s)
        p=Product.objects.create(name=n,cat=c,price=amt,status=s)
        #print(p)
        p.save()
        return redirect('/addproduct')
    
    else:
        #print("In else part")
        p=Product.objects.all()
        content={}
        content['products']=p
        return render(request,'addproduct.html',content) 

def delproduct(request,rid):
    #print("Id to be delete:",rid)  
    #fetch record to be deleted
    p=Product.objects.filter(id=rid)
    p.delete()
    return redirect('/addproduct')  

def editproduct(request,rid):

    if request.method=="POST":
        upname=request.POST['pname']
        ucat=request.POST['pcat']
        uprice=request.POST['pprice']
        ustatus=request.POST['status']

        #print(pname)
        #print(pcat)
        #print(pprice)
        #print(status)
        p=Product.objects.filter(id=rid)
        p.update(name=upname,cat=ucat,price=uprice,status=ustatus)
        return redirect('/addproduct')
    
    else:
        p=Product.objects.filter(id=rid)
        content={}
        content['product']=p
        return render(request,'editproduct.html',content)
    
def djangoform(request):
    if request=="POST":
        if request.method=="POST":
            ename=request.POST['name']
            dept=request.POST['dept']
            email=request.POST['email']
            sal=request.POST['salary']
            print("Employee Name:",ename)
            print("Deparment:",dept)
            print("Email:",email)
            print("salary:",sal)
        

    else:
        eobj=EmpForm()
        #print(eobj)
        content={}
        content['form']=eobj
        return render(request,'djangoform.html',content)
def modelform(request):
    if request.method=="POST":
        pass

    else:
        pobj=ProductModelForm()
        #print(pobj)
        content={}
        content['mform']=pobj
        return render(request,'modelform.html',content)
 
def user_register(request):

    if request.method=="POST":
        pass
    else:
        regobj=UserCreationForm()
        print(regobj)
        return HttpResponse()


    
   